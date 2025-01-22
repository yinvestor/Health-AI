from django import template
from django.forms import BoundField

register = template.Library()

@register.filter(name='add_class')
def add_class(value, css):
    if isinstance(value, BoundField):
        return value.as_widget(attrs={'class': css})
    return value

@register.filter(name='add_placeholder')
def add_placeholder(value, placeholder):
    if isinstance(value, BoundField):
        return value.as_widget(attrs={'placeholder': placeholder})
    return value
