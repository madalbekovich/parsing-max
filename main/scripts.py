import pandas as pd
import warnings
from datetime import datetime

from django.conf import settings
from main.models import Device

from django.utils import timezone

file_path = f'{settings.BASE_DIR}/data/data.xlsx'


def parsing():
    warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")

    sheets = {
        "ГУМ": pd.read_excel(file_path, sheet_name="ТЦ ГУМ", dtype=str).where(pd.notnull, None),
        "ЦУМ": pd.read_excel(file_path, sheet_name="ТЦ ЦУМ", dtype=str).where(pd.notnull, None),
    }

    objects = []

    def valid_date(date_str):
        if not date_str:
            return (False, False, None)
        try:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            return (False, False, None)
        limit_date = datetime(2024, 9, 4, 0, 0, 0)
        is_not_expired = date_obj <= limit_date
        return True, is_not_expired, date_obj

    def parse_gar(gar1, gar2):
        result = {
            "is_used": False,
            "display": False,
            "case": False,
            "general_360": False,
            "side": False,
            "lens": False,
        }
        combined = " ".join(filter(None, [gar1, gar2])).upper()
        if "ИСП" in combined:
            result["is_used"] = True
        if "ЭКР" in combined or "ЭКРАН" in combined:
            result["display"] = True
        if "КОРПУС" in combined or "КОРП" in combined:
            result["case"] = True
        if "360" in combined:
            result["general_360"] = True
        if "ТОРЦЫ" in combined or "БОКА" in combined:
            result["side"] = True
        if "ЛИНЗ" in combined:
            result["lens"] = True
        return result

    # Словарь соответствия столбцов для каждого листа
    columns_map = {
        "ГУМ": {
            "name": "ИМЯ",
            "phone": "НОМЕР",
            "date": "ДАТА",
            "model": "МОДЕЛЬ",
            "gar1": "ГАР-1",
            "gar2": "ГАР-2",
            "price": "ЦЕНА",
        },
        "ЦУМ": {
            "name": "Unnamed: 0",
            "phone": "Unnamed: 1",
            "date": "Unnamed: 2",
            "model": datetime.strptime("2025-04-18 00:00:00", "%Y-%m-%d %H:%M:%S"),
            "gar1": "Unnamed: 4",
            "gar2": "Unnamed: 5",
            "price": "Unnamed: 6",
        }
    }

    for where, data in sheets.items():
        cols = columns_map[where]
        for _, row in data.iterrows():
            date_value = row.get(cols["date"])
            is_valid, is_not_expired, date_obj = valid_date(date_value)
            if not is_valid:
                continue

            date_obj = timezone.make_aware(date_obj)

            obj = {
                "name": row.get(cols["name"]),
                "phone": row.get(cols["phone"]),
                "date": date_obj,
                "model": row.get(cols["model"]),
                "price": row.get(cols["price"]),
            }
            gar_flags = parse_gar(row.get(cols["gar1"]), row.get(cols["gar2"]))

            obj.update(gar_flags)

            if all(v is None for k, v in obj.items() if isinstance(v, str)) and not any(gar_flags.values()):
                continue

            obj["where"] = where

            if is_not_expired:
                obj["is_used"] = True

            objects.append(obj)

    device_objects = [Device(**obj) for obj in objects]
    Device.objects.bulk_create(device_objects)
