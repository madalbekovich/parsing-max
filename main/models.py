from django.db import models

class Device(models.Model):
    where = models.CharField(max_length=5, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    date = models.CharField(max_length=100, null=True, blank=True)
    model = models.CharField(max_length=255, null=True, blank=True)
    gar1 = models.CharField(max_length=255, null=True, blank=True)
    gar2 = models.CharField(max_length=255, null=True, blank=True)
    price = models.CharField(max_length=50, null=True, blank=True)
    lens = models.CharField(max_length=255, null=True, blank=True)
    ax = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Девайс"
        verbose_name_plural = "Девайсы"
