from django.db import models

class Product(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True)
    order_id = models.PositiveBigIntegerField()
    usd_price = models.DecimalField(max_digits=15, decimal_places=2)
    rub_price = models.DecimalField(max_digits=15, decimal_places=2)
    expiration = models.DateField()

    class Meta:
        ordering = ['-id']


class ProductHandler(models.Model):
    product_id = models.PositiveBigIntegerField()
    is_completed = models.BooleanField(default=False)
