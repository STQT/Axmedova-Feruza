"""
Telegram notifications для заказов
"""

import requests
from django.conf import settings


def send_telegram_message(message: str, parse_mode: str = 'HTML') -> bool:
    """
    Отправка сообщения в Telegram
    
    Args:
        message: Текст сообщения
        parse_mode: Режим форматирования ('HTML' или 'Markdown')
    
    Returns:
        bool: True если отправлено успешно, False если ошибка
    """
    
    # Проверяем настройки
    if not hasattr(settings, 'TELEGRAM_BOT_TOKEN') or not settings.TELEGRAM_BOT_TOKEN:
        print("⚠️  TELEGRAM_BOT_TOKEN не настроен в settings.py")
        return False
    
    if not hasattr(settings, 'TELEGRAM_CHAT_ID') or not settings.TELEGRAM_CHAT_ID:
        print("⚠️  TELEGRAM_CHAT_ID не настроен в settings.py")
        return False
    
    # URL Telegram Bot API
    url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
    
    # Параметры запроса
    payload = {
        'chat_id': settings.TELEGRAM_CHAT_ID,
        'text': message,
        'parse_mode': parse_mode,
    }
    
    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
        
        if response.json().get('ok'):
            print(f"✅ Telegram уведомление отправлено в chat_id: {settings.TELEGRAM_CHAT_ID}")
            return True
        else:
            print(f"❌ Ошибка Telegram API: {response.json()}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Ошибка при отправке в Telegram: {e}")
        return False


def format_service_order_message(order) -> str:
    """
    Форматирование сообщения для заказа услуги
    
    Args:
        order: Объект ServiceOrder
    
    Returns:
        str: Отформатированное сообщение
    """
    
    message = f"""
🔔 <b>Новый заказ услуги!</b>

📋 <b>Услуга:</b> {order.service.title}

👤 <b>Клиент:</b>
   • Имя: {order.full_name}
   • Email: {order.email}
   • Телефон: {order.phone}
"""
    
    if order.organization:
        message += f"   • Организация: {order.organization}\n"
    
    message += f"\n💬 <b>Описание запроса:</b>\n{order.message}\n"
    
    if order.preferred_date:
        message += f"\n📅 <b>Предпочтительная дата:</b> {order.preferred_date.strftime('%d.%m.%Y')}\n"
    
    message += f"\n⏰ <b>Дата заказа:</b> {order.created_at.strftime('%d.%m.%Y %H:%M')}"
    message += f"\n\n<i>ID заказа: #{order.id}</i>"
    
    return message


def format_book_order_message(order) -> str:
    """
    Форматирование сообщения для заказа книги
    
    Args:
        order: Объект BookOrder
    
    Returns:
        str: Отформатированное сообщение
    """
    
    message = f"""
📚 <b>Новый заказ книги!</b>

📖 <b>Книга:</b> {order.book.title}
   • Автор: {order.book.author}
   • Год: {order.book.publication_year}
"""
    
    if order.book.price:
        message += f"   • Цена: {order.book.price} руб.\n"
    
    message += f"   • Количество: {order.quantity} шт.\n"
    
    # Общая стоимость
    total = order.get_total_price()
    if total:
        message += f"   • <b>Итого:</b> {total} руб.\n"
    
    message += f"""
👤 <b>Клиент:</b>
   • Имя: {order.full_name}
   • Email: {order.email}
   • Телефон: {order.phone}

📍 <b>Адрес доставки:</b>
{order.address}
"""
    
    if order.message:
        message += f"\n💬 <b>Дополнительно:</b>\n{order.message}\n"
    
    message += f"\n⏰ <b>Дата заказа:</b> {order.created_at.strftime('%d.%m.%Y %H:%M')}"
    message += f"\n\n<i>ID заказа: #{order.id}</i>"
    
    return message


def notify_service_order(order):
    """
    Отправка уведомления о заказе услуги
    
    Args:
        order: Объект ServiceOrder
    """
    message = format_service_order_message(order)
    return send_telegram_message(message)


def notify_book_order(order):
    """
    Отправка уведомления о заказе книги
    
    Args:
        order: Объект BookOrder
    """
    message = format_book_order_message(order)
    return send_telegram_message(message)

