from django.db import models
from django.utils import timezone
from dateutil.relativedelta import relativedelta


class Device(models.Model):
    # Статусы для деталей
    STATUS_NOT_CHANGED = 'not_changed'
    STATUS_WITH_WARRANTY = 'with_warranty'
    STATUS_WARRANTY_USED = 'warranty_used'
    STATUS_WITHOUT_WARRANTY = 'without_warranty'

    PART_STATUS_CHOICES = [
        (STATUS_NOT_CHANGED, '❌ Не менялось'),
        (STATUS_WITH_WARRANTY, '✅ Заменено (гарантия)'),
        (STATUS_WARRANTY_USED, '⚠️ Гарантия использована'),
        (STATUS_WITHOUT_WARRANTY, '🔧 Без гарантии'),
    ]

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
    display_status = models.CharField(
        "Экран",
        max_length=20,
        choices=PART_STATUS_CHOICES,
        default=STATUS_NOT_CHANGED
    )
    display_warranty_date = models.DateField("Дата окончания гарантии", null=True, blank=True)
    display_used_date = models.DateField("Дата использования гарантии", null=True, blank=True)

    # --- КОРПУС ---
    case_status = models.CharField(
        "Корпус",
        max_length=20,
        choices=PART_STATUS_CHOICES,
        default=STATUS_NOT_CHANGED
    )
    case_warranty_date = models.DateField("Дата окончания гарантии", null=True, blank=True)
    case_used_date = models.DateField("Дата использования гарантии", null=True, blank=True)

    # --- КРЫШКА ---
    cover_status = models.CharField(
        "Крышка",
        max_length=20,
        choices=PART_STATUS_CHOICES,
        default=STATUS_NOT_CHANGED
    )
    cover_warranty_date = models.DateField("Дата окончания гарантии", null=True, blank=True)
    cover_used_date = models.DateField("Дата использования гарантии", null=True, blank=True)

    # --- 360 ---
    general_360_status = models.CharField(
        "360 (полная оклейка)",
        max_length=20,
        choices=PART_STATUS_CHOICES,
        default=STATUS_NOT_CHANGED
    )
    general_360_warranty_date = models.DateField("Дата окончания гарантии", null=True, blank=True)
    general_360_used_date = models.DateField("Дата использования гарантии", null=True, blank=True)

    # --- БОКОВАЯ ЧАСТЬ ---
    side_status = models.CharField(
        "Боковая часть",
        max_length=20,
        choices=PART_STATUS_CHOICES,
        default=STATUS_NOT_CHANGED
    )
    side_warranty_date = models.DateField("Дата окончания гарантии", null=True, blank=True)
    side_used_date = models.DateField("Дата использования гарантии", null=True, blank=True)

    # --- ЛИНЗЫ ---
    lens_status = models.CharField(
        "Линзы",
        max_length=20,
        choices=PART_STATUS_CHOICES,
        default=STATUS_NOT_CHANGED
    )
    lens_warranty_date = models.DateField("Дата окончания гарантии", null=True, blank=True)
    lens_used_date = models.DateField("Дата использования гарантии", null=True, blank=True)

    created_at = models.DateTimeField("Дата создания", auto_now_add=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        """
        Упрощённая логика:
        - Если выбрана полная оклейка (360), то остальные детали получают тот же статус.
        - При статусе "с гарантией" → +1 год.
        - При статусе "гарантия использована" → фиксируется дата.
        """
        today = timezone.now().date()

        # Получаем старую версию
        old_instance = None
        if self.pk:
            try:
                old_instance = Device.objects.get(pk=self.pk)
            except Device.DoesNotExist:
                pass

        # Универсальная обработка деталей
        parts = [
            ('display_status', 'display_warranty_date', 'display_used_date'),
            ('case_status', 'case_warranty_date', 'case_used_date'),
            ('cover_status', 'cover_warranty_date', 'cover_used_date'),
            ('general_360_status', 'general_360_warranty_date', 'general_360_used_date'),
            ('side_status', 'side_warranty_date', 'side_used_date'),
            ('lens_status', 'lens_warranty_date', 'lens_used_date'),
        ]

        # 1️⃣ Если клиент выбрал "360", применяем этот статус ко всем деталям
        if self.general_360_status != self.STATUS_NOT_CHANGED:
            for field, _, _ in parts:
                if field != 'general_360_status':
                    setattr(self, field, self.general_360_status)

        # 2️⃣ Обрабатываем каждую деталь
        for status_field, warranty_field, used_field in parts:
            status = getattr(self, status_field)

            if status == self.STATUS_WITH_WARRANTY:
                if not getattr(self, warranty_field):
                    setattr(self, warranty_field, today + relativedelta(years=1))
                setattr(self, used_field, None)

            elif status == self.STATUS_WARRANTY_USED:
                if not getattr(self, used_field):
                    setattr(self, used_field, today)

            elif status in [self.STATUS_NOT_CHANGED, self.STATUS_WITHOUT_WARRANTY]:
                setattr(self, warranty_field, None)
                if status == self.STATUS_NOT_CHANGED:
                    setattr(self, used_field, None)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.phone} ({self.model})"

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"