from celery import shared_task
from product import gsheets_integration
from product import telegram_integration


@shared_task
def create_update_delete_product():
    return gsheets_integration.create_update_delete_product()

@shared_task
def send_message(product_id):
    return telegram_integration.send_message(product_id)