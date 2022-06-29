import requests

from django.conf import settings

from .models import Product, ProductHandler

SEND_MESSAGE = "/sendMessage"

def send_message(product_id):
    """Sending message from Telegram Bot to Client"""
    
    if settings.TELEGRAM_BOT_URL and settings.TELEGRAM_CHAT_ID:
        message = {}
        message["chat_id"] = settings.TELEGRAM_CHAT_ID
        message["text"] = f'the product №{product_id}: delivery period has expired!'

        resp = requests.post(url=f"{settings.TELEGRAM_BOT_URL}{SEND_MESSAGE}", json=message)
        resp.raise_for_status()

    product_handler = ProductHandler.objects.get(product_id=product_id)
    product_handler.is_completed = True
    product_handler.save()