from django import template

from ..models import Settings

register = template.Library()

@register.simple_tag
def get_config(key):
    try:
        config = Settings.objects.get(key=key)
        return config.value
    except Settings.DoesNotExist:
        return ''
