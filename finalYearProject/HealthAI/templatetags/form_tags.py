from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(value, css):
    return value.as_widget(attrs={'class': css})

@register.filter(name='add_placeholder')
def add_placeholder(value, placeholder):
    return value.as_widget(attrs={'placeholder': placeholder})


