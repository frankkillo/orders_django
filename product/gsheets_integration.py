from .models import Product, ProductHandler
from gsheets.django_client import get_client_from_settings


def create_update_delete_product():
    """
    Get data from Google Sheets Table and sync with database
    """
    gsheet_client = get_client_from_settings()
    
    products_set = set()

    for product in gsheet_client.records():
        obj, created = Product.objects.update_or_create(
            id=product.id, defaults={
                'id':product.id,
                'order_id':product.order_id,
                'usd_price':product.usd_price,
                'rub_price':product.rub_price,
                'expiration':product.expiration
            }
        )

        products_set.add(product.id)

    all_products_set = set(i[0] for i in Product.objects.values_list('id'))
    products_to_del = list(all_products_set - products_set)

    Product.objects.filter(id__in=products_to_del).delete()
    
