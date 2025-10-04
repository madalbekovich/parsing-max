from django.db import models
import random

class Device(models.Model):
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
    date = models.CharField(
        "Дата",
        max_length=255,
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
    gar1 = models.BooleanField(
        "Экран",
        default=random.choice([True, False])
    )
    gar2 = models.BooleanField(
        "Корпус",
        default=random.choice([True, False])
    )
    general_360 = models.BooleanField(
        "360",
        default=random.choice([True, False])
    )
    side = models.BooleanField(
        "Бокавая часть",
        default=random.choice([True, False])
    )
    lens = models.BooleanField(
        verbose_name='Линзы',
        default=random.choice([True, False])
    )

    is_used = models.BooleanField(
        "Просрочка",
        default=random.choice([True, False])
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создание',
        # auto_now_add=True,
        null=True,
        blank=True
    )
    class Meta:
        verbose_name = "Девайс"
        verbose_name_plural = "Девайсы"
