# name = None
# number = None
# date = None
# gar1 = None
# gar2 = None
# price = None
# lens = None
# ax = None

import pandas as pd
import warnings

from django.conf import settings
from main.models import Device

file_path = f'{settings.BASE_DIR}/data/data.xlsx'

def parsing():
    warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")

    data_gum = pd.read_excel(file_path, sheet_name="ТЦ ГУМ", dtype=str).where(pd.notnull, None)
    data_tsum = pd.read_excel(file_path, sheet_name="ТЦ ЦУМ", dtype=str).where(pd.notnull, None)

    objects = []

    for _, row in data_gum.iterrows():
        obj = {
            "name": row.get("ИМЯ"),
            "phone": row.get("НОМЕР"),
            "date": row.get("ДАТА"),
            "model": row.get("МОДЕЛЬ"),
            "gar1": row.get("ГАР-1"),
            "gar2": row.get("ГАР-2"),
            "price": row.get("ЦЕНА"),
            "lens": row.get("ЛИНЗА"),
            "ax": row.get("AX"),
        }

        if all(v is None for v in obj.values()):
            continue

        obj["where"] = "ГУМ"

        objects.append(obj)

    for _, row in data_tsum.iterrows():
        obj = {
            "name": row.get("Unnamed: 0"),
            "phone": row.get("Unnamed: 1"),
            "date": row.get("Unnamed: 2"),
            "model": row.get("2025-04-18 00:00:00") or row.get("Unnamed: 3"),
            "gar1": row.get("Unnamed: 4"),
            "gar2": row.get("Unnamed: 5"),
            "price": row.get("Unnamed: 6"),
            "lens": None,
            "ax": None,
        }

        if all(v is None for v in obj.values()):
            continue

        obj["where"] = "ЦУМ"

        objects.append(obj)

    device_objects = [Device(**obj) for obj in objects]

    Device.objects.bulk_create(device_objects)
