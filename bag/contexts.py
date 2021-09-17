from decimal import Decimal
from django.conf import settings

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGES/100)
        FREE_DELIVERY_DELTA = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        FREE_DELIVERY_DELTA = 0
    
    grand_total = delivery + total

    context = {}

    return context
