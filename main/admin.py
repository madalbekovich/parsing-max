from django.contrib import admin
from django.contrib.auth.models import User, Group
from django import forms
from django.utils.html import format_html
from .models import Device

admin.site.unregister(User)
admin.site.unregister(Group)


class DeviceAdminForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = '__all__'
        widgets = {
            # Выпадающие списки для статусов (красивые select)
            'display_status': forms.Select(attrs={'class': 'status-select'}),
            'case_status': forms.Select(attrs={'class': 'status-select'}),
            'cover_status': forms.Select(attrs={'class': 'status-select'}),
            'general_360_status': forms.Select(attrs={'class': 'status-select'}),
            'side_status': forms.Select(attrs={'class': 'status-select'}),
            'lens_status': forms.Select(attrs={'class': 'status-select'}),
        }


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    form = DeviceAdminForm

    list_display = [
        'where', 'name', 'phone', 'date', 'model',
        'display_status_display', 'case_status_display',
        'cover_status_display', 'general_360_status_display',
        'side_status_display', 'lens_status_display',
        'price', 'is_used'
    ]
    list_display_links = ['where', 'name', 'phone', 'date', 'model']
    list_filter = ('where', 'date', 'display_status', 'case_status')
    search_fields = ['name', 'phone', 'model']

    readonly_fields = (
        "display_warranty_date",
        "display_used_date",
        "case_warranty_date",
        "case_used_date",
        "cover_warranty_date",
        "cover_used_date",
        "general_360_warranty_date",
        "general_360_used_date",
        "side_warranty_date",
        "side_used_date",
        "lens_warranty_date",
        "lens_used_date",
        "created_at",
    )

    fieldsets = (
        ("Общая информация", {
            "fields": (
                "is_used",
                "where",
                "name",
                "phone",
                "date",
                "model",
                "price",
            )
        }),
        ("Детали ремонта / гарантий", {
            "fields": (
                ("display_status", "display_warranty_date", "display_used_date"),
                ("case_status", "case_warranty_date", "case_used_date"),
                ("cover_status", "cover_warranty_date", "cover_used_date"),
                ("general_360_status", "general_360_warranty_date", "general_360_used_date"),
                ("side_status", "side_warranty_date", "side_used_date"),
                ("lens_status", "lens_warranty_date", "lens_used_date"),
            ),
            "classes": ("wide", "repair-details-section"),
            "description": "💡 Выберите статус для каждой детали. При выборе 'Заменено (гарантия)' автоматически установится дата окончания гарантии."
        }),
        ("Служебная информация", {
            "fields": ("created_at",),
        }),
    )

    class Media:
        css = {
            'all': ('admin/css/repair_details_simple.css',)
        }
        js = ('admin/js/warranty_simple.js',)

    # Красивое отображение статусов в списке
    def display_status_display(self, obj):
        return self._get_status_badge(obj.display_status)

    display_status_display.short_description = "Экран"

    def case_status_display(self, obj):
        return self._get_status_badge(obj.case_status)

    case_status_display.short_description = "Корпус"

    def cover_status_display(self, obj):
        return self._get_status_badge(obj.cover_status)

    cover_status_display.short_description = "Крышка"

    def general_360_status_display(self, obj):
        return self._get_status_badge(obj.general_360_status)

    general_360_status_display.short_description = "360"

    def side_status_display(self, obj):
        return self._get_status_badge(obj.side_status)

    side_status_display.short_description = "Боковая"

    def lens_status_display(self, obj):
        return self._get_status_badge(obj.lens_status)

    lens_status_display.short_description = "Линзы"

    def _get_status_badge(self, status):
        """Возвращает красивый badge для статуса"""
        badges = {
            'not_changed': '<span style="color: #6c757d;">❌</span>',
            'with_warranty': '<span style="color: #28a745; font-weight: bold;">✅</span>',
            'warranty_used': '<span style="color: #ffc107; font-weight: bold;">⚠️</span>',
            'without_warranty': '<span style="color: #007bff;">🔧</span>',
        }
        return format_html(badges.get(status, status))

    def get_form(self, request, obj=None, **kwargs):
        """Добавляем подсказки к полям"""
        form = super().get_form(request, obj, **kwargs)

        # Подсказки для полей статуса
        status_help = {
            'display_status': 'Выберите статус экрана. При выборе "Заменено (гарантия)" автоматически установится срок на 1 год.',
            'case_status': 'Выберите статус корпуса.',
            'cover_status': 'Выберите статус крышки.',
            'general_360_status': 'Полная оклейка устройства. При выборе этого варианта остальные детали можно не заполнять.',
            'side_status': 'Выберите статус боковой части.',
            'lens_status': 'Выберите статус линз.',
        }

        for field_name, help_text in status_help.items():
            if field_name in form.base_fields:
                form.base_fields[field_name].help_text = help_text

        return form