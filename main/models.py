from django.db import models
import random

class Device(models.Model):
    is_used = models.BooleanField(
        "Просрочка",
        default=False
    )
    where = models.CharField(
        "где",
        max_length=5,
        null=True,
        blank=True,
        choices=(
            ("ЦУМ", "ЦУМ"),
            ("ГУМ", "ГУМ"),
        ))
    name = models.CharField(
        "ФИО",
        max_length=255,
        null=True,
        blank=True
    )
    phone = models.CharField(
        "Телефон",
        max_length=255,
        null=True,
        blank=True
    )
    date = models.DateTimeField(
        "Дата",
        null=True,
        blank=True
    )
    model = models.CharField(
        "Модель",
        max_length=255,
        null=True,
        blank=True
    )
    price = models.CharField(
        "Цена",
        max_length=255,
        null=True,
        blank=True
    )
    display = models.BooleanField(
        "Экран",
        default=False
    )
    case = models.BooleanField(
        "Корпус",
        default=False
    )
    general_360 = models.BooleanField(
        "360",
        default=False
    )
    side = models.BooleanField(
        "Бокавая часть",
        default=False
    )
    lens = models.BooleanField(
        verbose_name='Линзы',
        default=False
    )

    created_at = models.DateTimeField(
        verbose_name='Дата создание',
        auto_now_add=True,
        null=True,
        blank=True
    )
    class Meta:
        verbose_name = "Девайс"
        verbose_name_plural = "Девайсы"
