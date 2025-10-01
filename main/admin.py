from django.utils.html import format_html
from django.contrib import admin
from django.contrib.auth.models import User, Group

from .models import Device

admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['colored_row', 'name', 'phone', 'date', 'model', 'gar1', 'gar2', 'price', 'lens', 'ax']
    list_display_links = ['colored_row', 'name', 'phone', 'date', 'model']

    def colored_row(self, obj):
        if (obj.gar1 and 'ИСП' in obj.gar1.upper()) or (obj.gar2 and 'ИСП' in obj.gar2.upper()):
            color = '#F08080'
        else:
            color = '#00ff00'

        return format_html(
            '<div style="background-color: {}; display: block; width: 100%; padding: 5px;">{}</div>',
            color,
            obj.where
        )

    colored_row.short_description = 'Где'


    def active_filter(self, obj):
        return not ((obj.gar1 and 'ИСП' in obj.gar1.upper()) or (obj.gar2 and 'ИСП' in obj.gar2.upper()))

    active_filter.boolean = True
    active_filter.short_description = 'Активный'

class ActiveFilter(admin.SimpleListFilter):
    title = 'гарантии'
    parameter_name = 'active'

    def lookups(self, request, model_admin):
        return (
            ('active', 'Не использованные'),
            ('inactive', 'Использованные'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'active':
            return queryset.exclude(gar1__icontains='ИСП').exclude(gar2__icontains='ИСП')
        if self.value() == 'inactive':
            return queryset.filter(gar1__icontains='ИСП') | queryset.filter(gar2__icontains='ИСП')
        return queryset


DeviceAdmin.list_filter = (ActiveFilter, 'where')