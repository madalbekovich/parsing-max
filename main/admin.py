# from django.utils.html import format_html
# from django.contrib import admin
# from django.contrib.auth.models import User, Group
# from .models import Device

# admin.site.unregister(User)
# admin.site.unregister(Group)

# @admin.register(Device)
# class DeviceAdmin(admin.ModelAdmin):
#     list_display = ['where', 'name', 'phone', 'date', 'model', 'display', 'case', 'cover', 'general_360', 'side', 'price', 'lens', 'is_used']
#     list_display_links = ['where', 'name', 'phone', 'date', 'model']
#     list_filter = ('where', 'date')
#     search_fields = ['name', 'phone', 'model']
#     readonly_fields = (
#     #     "display_date",
#     #     "case_date",
#     #     "cover_date",
#     #     "general_360_date",
#     #     "side_date",
#     #     "lens_date",
#         "created_at",
#     )
#     fieldsets = (
#         ("Общая информация", {
#             "fields": (
#                 "is_used",
#                 "where",
#                 "name",
#                 "phone",
#                 "date",
#                 "model",
#                 "price",
#             )
#         }),
#         ("Детали ремонта / гарантий", {
#             "fields": (
#                 ("display", "display_date"),
#                 ("case", "case_date"),
#                 ("cover", "cover_date"),
#                 ("general_360", "general_360_date"),
#                 ("side", "side_date"),
#                 ("lens", "lens_date"),
#             )
#         }),
#         ("Служебная информация", {
#             "fields": ("created_at",),
#         }),
#     )

from django.utils.html import format_html
from django.contrib import admin
from django.contrib.auth.models import User, Group
from django import forms
from .models import Device

admin.site.unregister(User)
admin.site.unregister(Group)


class DeviceAdminForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = '__all__'
        widgets = {
            # Экран
            'display': forms.CheckboxInput(attrs={'class': 'inline-checkbox'}),
            'display_warranty': forms.CheckboxInput(attrs={'class': 'inline-checkbox'}),
            'display_date': forms.DateInput(attrs={'type': 'date', 'class': 'inline-date'}),
            # Корпус
            'case': forms.CheckboxInput(attrs={'class': 'inline-checkbox'}),
            'case_warranty': forms.CheckboxInput(attrs={'class': 'inline-checkbox'}),
            'case_date': forms.DateInput(attrs={'type': 'date', 'class': 'inline-date'}),
            # Крышка
            'cover': forms.CheckboxInput(attrs={'class': 'inline-checkbox'}),
            'cover_warranty': forms.CheckboxInput(attrs={'class': 'inline-checkbox'}),
            'cover_date': forms.DateInput(attrs={'type': 'date', 'class': 'inline-date'}),
            # 360
            'general_360': forms.CheckboxInput(attrs={'class': 'inline-checkbox'}),
            'general_360_warranty': forms.CheckboxInput(attrs={'class': 'inline-checkbox'}),
            'general_360_date': forms.DateInput(attrs={'type': 'date', 'class': 'inline-date'}),
            # Боковая часть
            'side': forms.CheckboxInput(attrs={'class': 'inline-checkbox'}),
            'side_warranty': forms.CheckboxInput(attrs={'class': 'inline-checkbox'}),
            'side_date': forms.DateInput(attrs={'type': 'date', 'class': 'inline-date'}),
            # Линзы
            'lens': forms.CheckboxInput(attrs={'class': 'inline-checkbox'}),
            'lens_warranty': forms.CheckboxInput(attrs={'class': 'inline-checkbox'}),
            'lens_date': forms.DateInput(attrs={'type': 'date', 'class': 'inline-date'}),
        }


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    form = DeviceAdminForm
    
    list_display = [
        'where', 'name', 'phone', 'date', 'model', 'price',
        'display', 'case', 'cover', 'general_360', 
        'side', 'lens', 'is_used'
    ]
    list_display_links = ['where', 'name', 'phone', 'date', 'model']
    list_filter = ('where', 'date')
    search_fields = ['name', 'phone', 'model']
    readonly_fields = (
        "used_display_date",
        "used_case_date",
        "used_cover_date",
        "used_general_360_date",
        "used_side_date",
        "used_lens_date",
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
                ("display", "display_warranty", "display_date", "used_display_date"),
                ("case", "case_warranty", "case_date", "used_case_date"),
                ("cover", "cover_warranty", "cover_date", "used_cover_date"),
                ("general_360", "general_360_warranty", "general_360_date", "used_general_360_date"),
                ("side", "side_warranty", "side_date", "used_side_date"),
                ("lens", "lens_warranty", "lens_date", "used_lens_date"),
            ),
            "classes": ("wide", "repair-details-fieldset"),
        }),
        ("Служебная информация", {
            "fields": ("created_at",),
        }),
    )

    class Media:
        css = {
            'all': ('admin/css/repair_details_inline.css',)
        }
        js = (
            'admin/js/repair_details_helper.js',
            'admin/js/warranty_logic.js',
        )
    
    def get_form(self, request, obj=None, **kwargs):
        """Переопределяем форму для правильного отображения дат"""
        form = super().get_form(request, obj, **kwargs)
        
        date_fields = [
            'display_date', 'case_date', 'cover_date',
            'general_360_date', 'side_date', 'lens_date'
        ]
        
        for field_name in date_fields:
            if field_name in form.base_fields:
                form.base_fields[field_name].input_formats = ['%Y-%m-%d']
                form.base_fields[field_name].widget.format = '%Y-%m-%d'
        
        return form