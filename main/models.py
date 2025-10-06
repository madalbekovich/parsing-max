from django.db import models
import random
from django.utils import timezone
from datetime import timedelta

class Device(models.Model):
    is_used = models.BooleanField(
        "Просрочка/ИСП",
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
    display_date = models.DateField(
        "Гарантия экрана",
        null=True,
        blank=True,
    )
    case = models.BooleanField(
        "Корпус",
        default=False
    )
    case_date = models.DateField(
        "Гарантия корпуса",
        null=True,
        blank=True,
    )
    cover = models.BooleanField(
        "Крышка",
        default=False
    )
    cover_date = models.DateField(
        "Гарантия крышки",
        null=True,
        blank=True,
    )
    general_360 = models.BooleanField(
        "360",
        default=False
    )
    general_360_date = models.DateField(
        "Гарантия 360",
        null=True,
        blank=True,
    )
    side = models.BooleanField(
        "Бокавая часть",
        default=False
    )
    side_date = models.DateField(
        "Гарантия боковой части",
        null=True,
        blank=True,
    )
    lens = models.BooleanField(
        verbose_name='Линзы',
        default=False
    )
    lens_date = models.DateField(
        "Гарантия линзы",
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        verbose_name='Дата создание',
        auto_now_add=True,
        null=True,
        blank=True
    )

    # def save(self, *args, **kwargs):
    #     next_year = (timezone.now() + timedelta(days=365)).date()
    #
    #     if self.display and not self.display_date:
    #         self.display_date = next_year
    #
    #     if self.case and not self.case_date:
    #         self.cas_date = next_year
    #
    #     if self.cover and not self.cover_date:
    #         self.cover_date = next_year
    #
    #     if self.general_360 and not self.general_360_date:
    #         self.general_360_date = next_year
    #
    #     if self.side and not self.side_date:
    #         self.side_date = next_year
    #
    #     if self.lens and not self.lens_date:
    #         self.lens_date = next_year
    #
    #     super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Клиента"
        verbose_name_plural = "Клиенты"
