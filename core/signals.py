"""
Django signals для автоматических действий
"""

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ServiceOrder, BookOrder
from .telegram_notifications import notify_service_order, notify_book_order


@receiver(post_save, sender=ServiceOrder)
def service_order_created(sender, instance, created, **kwargs):
    """
    Signal handler для создания заказа услуги
    Отправляет уведомление в Telegram при создании нового заказа
    """
    if created:  # Только для новых заказов
        try:
            notify_service_order(instance)
        except Exception as e:
            print(f"❌ Ошибка при отправке уведомления о заказе услуги: {e}")


@receiver(post_save, sender=BookOrder)
def book_order_created(sender, instance, created, **kwargs):
    """
    Signal handler для создания заказа книги
    Отправляет уведомление в Telegram при создании нового заказа
    """
    if created:  # Только для новых заказов
        try:
            notify_book_order(instance)
        except Exception as e:
            print(f"❌ Ошибка при отправке уведомления о заказе книги: {e}")

