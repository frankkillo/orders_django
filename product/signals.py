from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from .models import Product, ProductHandler
from .tasks import send_message

@receiver(post_save, sender=Product, dispatch_uid="product_expiration_status")
def check_product_expiration(sender, instance, **kwargs):
    """
    if the product delivery time has expired, we will send a message to the client 
    """
    if instance.expiration < timezone.now().date():
        ph, created = ProductHandler.objects.get_or_create(product_id=instance.id)
        if not ph.is_completed:
            send_message.delay(instance.id)