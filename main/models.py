from django.db import models

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
        "Имя",
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
    gar1 = models.CharField(
        "Гар 1",
        max_length=255,
        null=True,
        blank=True
    )
    gar2 = models.CharField(
        "Гар 2",
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
    lens = models.CharField(
        "Линзы",
        max_length=255,
        null=True,
        blank=True
    )
    ax = models.CharField(
        "Ax",
        max_length=255,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Девайс"
        verbose_name_plural = "Девайсы"
