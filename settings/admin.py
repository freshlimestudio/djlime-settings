from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from models import Settings

_('Settings')

class SettingsAdmin(admin.ModelAdmin):
    list_display = ('key', 'value',)

admin.site.register(Settings, SettingsAdmin)