from django.contrib import admin

from .models import Product, ProductHandler

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['id', 'order_id', 'usd_price', 'rub_price', 'expiration']

admin.site.register(ProductHandler)