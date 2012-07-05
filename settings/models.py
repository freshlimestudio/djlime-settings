from django.db import models
from django.utils.translation import ugettext_lazy as _

class Settings(models.Model):
    key = models.CharField(_('key'), max_length=255)
    value = models.TextField(_('value'))

    class Meta:
        db_table = 'settings'
        verbose_name = _('setting')
        verbose_name_plural = _('settings')

    def __unicode__(self):
        return self.key
