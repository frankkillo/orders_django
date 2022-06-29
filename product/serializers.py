from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "order_id",
            "usd_price",
            "rub_price",
            "expiration"
        ]