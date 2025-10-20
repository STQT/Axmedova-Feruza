"""Custom template filters"""
from django import template

register = template.Library()


@register.filter(name='split_tags')
def split_tags(value, delimiter=','):
    """Split a string by delimiter and strip whitespace"""
    if not value:
        return []
    return [tag.strip() for tag in value.split(delimiter) if tag.strip()]


@register.filter
def format_price(price):
    """
    Форматирование цены с валютой
    Если цена - число, добавляет "сум", иначе выводит как есть
    """
    if not price:
        return ""
    
    price_str = str(price).strip()
    
    # Проверяем, является ли цена числом
    if price_str.isdigit():
        # Форматируем число с пробелами (разделитель тысяч)
        price_int = int(price_str)
        formatted = f"{price_int:,}".replace(',', ' ')
        return f"{formatted} сум"
    else:
        # Возвращаем как есть (например, "Договорная")
        return price_str

