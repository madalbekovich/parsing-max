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