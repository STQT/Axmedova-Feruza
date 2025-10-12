"""Custom template filters"""
from django import template

register = template.Library()


@register.filter(name='split_tags')
def split_tags(value, delimiter=','):
    """Split a string by delimiter and strip whitespace"""
    if not value:
        return []
    return [tag.strip() for tag in value.split(delimiter) if tag.strip()]

