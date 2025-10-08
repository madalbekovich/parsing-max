# from django.db import models
# import random
# from django.utils import timezone
# from datetime import timedelta

# class Device(models.Model):
#     is_used = models.BooleanField(
#         "Просрочка/ИСП",
#         default=False
#     )
#     where = models.CharField(
#         "где",
#         max_length=5,
#         null=True,
#         blank=True,
#         choices=(
#             ("ЦУМ", "ЦУМ"),
#             ("ГУМ", "ГУМ"),
#         ))
#     name = models.CharField(
#         "ФИО",
#         max_length=255,
#         null=True,
#         blank=True
#     )
#     phone = models.CharField(
#         "Телефон",
#         max_length=255,
#         null=True,
#         blank=True
#     )
#     date = models.DateTimeField(
#         "Дата",
#         null=True,
#         blank=True
#     )
#     model = models.CharField(
#         "Модель",
#         max_length=255,
#         null=True,
#         blank=True
#     )
#     price = models.CharField(
#         "Цена",
#         max_length=255,
#         null=True,
#         blank=True
#     )
#     display = models.BooleanField(
#         "Экран",
#         default=False
#     )
#     display_date = models.DateField(
#         "Гарантия экрана",
#         null=True,
#         blank=True,
#     )
#     case = models.BooleanField(
#         "Корпус",
#         default=False
#     )
#     case_date = models.DateField(
#         "Гарантия корпуса",
#         null=True,
#         blank=True,
#     )
#     cover = models.BooleanField(
#         "Крышка",
#         default=False
#     )
#     cover_date = models.DateField(
#         "Гарантия крышки",
#         null=True,
#         blank=True,
#     )
#     general_360 = models.BooleanField(
#         "360",
#         default=False
#     )
#     general_360_date = models.DateField(
#         "Гарантия 360",
#         null=True,
#         blank=True,
#     )
#     side = models.BooleanField(
#         "Бокавая часть",
#         default=False
#     )
#     side_date = models.DateField(
#         "Гарантия боковой части",
#         null=True,
#         blank=True,
#     )
#     lens = models.BooleanField(
#         verbose_name='Линзы',
#         default=False
#     )
#     lens_date = models.DateField(
#         "Гарантия линзы",
#         null=True,
#         blank=True,
#     )

#     created_at = models.DateTimeField(
#         verbose_name='Дата создание',
#         auto_now_add=True,
#         null=True,
#         blank=True
#     )

#     # def save(self, *args, **kwargs):
#     #     next_year = (timezone.now() + timedelta(days=365)).date()
#     #
#     #     if self.display and not self.display_date:
#     #         self.display_date = next_year
#     #
#     #     if self.case and not self.case_date:
#     #         self.cas_date = next_year
#     #
#     #     if self.cover and not self.cover_date:
#     #         self.cover_date = next_year
#     #
#     #     if self.general_360 and not self.general_360_date:
#     #         self.general_360_date = next_year
#     #
#     #     if self.side and not self.side_date:
#     #         self.side_date = next_year
#     #
#     #     if self.lens and not self.lens_date:
#     #         self.lens_date = next_year
#     #
#     #     super().save(*args, **kwargs)

#     class Meta:
#         verbose_name = "Клиента"
#         verbose_name_plural = "Клиенты"




from django.db import models
from django.utils import timezone


class Device(models.Model):
    # Общие данные
    is_used = models.BooleanField("Просрочка/ИСП", default=False)
    where = models.CharField("где", max_length=5, null=True, blank=True,
                             choices=(("ЦУМ", "ЦУМ"), ("ГУМ", "ГУМ")))
    name = models.CharField("ФИО", max_length=255, null=True, blank=True)
    phone = models.CharField("Телефон", max_length=255, null=True, blank=True)
    date = models.DateTimeField("Дата", null=True, blank=True)
    model = models.CharField("Модель", max_length=255, null=True, blank=True)
    price = models.CharField("Цена", max_length=255, null=True, blank=True)

    # --- ЭКРАН ---
    display = models.BooleanField("Экран", default=False)
    display_warranty = models.BooleanField("Гарантия экрана", default=False)
    display_date = models.DateField("Дата гарантии экрана", null=True, blank=True)
    used_display_date = models.DateField("Использовано экран", null=True, blank=True)

    # --- КОРПУС ---
    case = models.BooleanField("Корпус", default=False)
    case_warranty = models.BooleanField("Гарантия корпуса", default=False)
    case_date = models.DateField("Дата гарантии корпуса", null=True, blank=True)
    used_case_date = models.DateField("Использовано корпус", null=True, blank=True)

    # --- КРЫШКА ---
    cover = models.BooleanField("Крышка", default=False)
    cover_warranty = models.BooleanField("Гарантия крышки", default=False)
    cover_date = models.DateField("Дата гарантии крышки", null=True, blank=True)
    used_cover_date = models.DateField("Использовано крышка", null=True, blank=True)

    # --- 360 ---
    general_360 = models.BooleanField("360", default=False)
    general_360_warranty = models.BooleanField("Гарантия 360", default=False)
    general_360_date = models.DateField("Дата гарантии 360", null=True, blank=True)
    used_general_360_date = models.DateField("Использовано 360", null=True, blank=True)

    # --- БОКОВАЯ ЧАСТЬ ---
    side = models.BooleanField("Боковая часть", default=False)
    side_warranty = models.BooleanField("Гарантия боковой части", default=False)
    side_date = models.DateField("Дата гарантии боковой части", null=True, blank=True)
    used_side_date = models.DateField("Использовано боковая часть", null=True, blank=True)

    # --- ЛИНЗЫ ---
    lens = models.BooleanField("Линзы", default=False)
    lens_warranty = models.BooleanField("Гарантия линзы", default=False)
    lens_date = models.DateField("Дата гарантии линзы", null=True, blank=True)
    used_lens_date = models.DateField("Использовано линзы", null=True, blank=True)

    created_at = models.DateTimeField("Дата создания", auto_now_add=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        today = timezone.now().date()

        old_instance = None
        if self.pk:
            try:
                old_instance = Device.objects.get(pk=self.pk)
            except Device.DoesNotExist:
                pass

        warranty_fields = [
            ("display_warranty", "used_display_date"),
            ("case_warranty", "used_case_date"),
            ("cover_warranty", "used_cover_date"),
            ("general_360_warranty", "used_general_360_date"),
            ("side_warranty", "used_side_date"),
            ("lens_warranty", "used_lens_date"),
        ]

        for warranty_field, used_field in warranty_fields:
            current_warranty = getattr(self, warranty_field)
            current_used = getattr(self, used_field)
            
            if not old_instance:
                continue
            
            old_warranty = getattr(old_instance, warranty_field)
            old_used = getattr(old_instance, used_field)
            
            # СЛУЧАЙ 1: Гарантия ОТКЛЮЧИЛАСЬ (было True -- стало False)
            if old_warranty and not current_warranty:
                if not current_used:
                    setattr(self, used_field, today)
            
            elif not old_warranty and current_warranty:
                setattr(self, used_field, None)
            

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"