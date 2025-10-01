from django.contrib.auth.models import User, Group
from django.contrib import admin
from .models import Device

admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'date', 'model', 'gar1', 'gar2', 'price', 'lens', 'ax']
    list_display_links = list_display
