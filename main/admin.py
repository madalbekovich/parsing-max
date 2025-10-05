from django.utils.html import format_html
from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Device

admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['where', 'name', 'phone', 'date', 'model', 'display', 'case', 'cover', 'general_360', 'side', 'price', 'lens', 'is_used']
    list_display_links = ['where', 'name', 'phone', 'date', 'model']
    list_filter = ('where', 'date')
    search_fields = ['name', 'phone', 'model']
    readonly_fields = (
        "display_date",
        "case_date",
        "cover_date",
        "general_360_date",
        "side_date",
        "lens_date",
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
                ("display", "display_date"),
                ("case", "case_date"),
                ("cover", "cover_date"),
                ("general_360", "general_360_date"),
                ("side", "side_date"),
                ("lens", "lens_date"),
            )
        }),
        ("Служебная информация", {
            "fields": ("created_at",),
        }),
    )