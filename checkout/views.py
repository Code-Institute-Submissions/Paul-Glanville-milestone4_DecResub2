from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in the bag right now.")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JEEjOHf5taf5Ecwfi2go5EHQPyhpsVbRsB233hT2BQG8ExVbIUblZcBrA5faWfS0bLERAMiFv2B4K1Igx80uQj800PQV9HdmK',
    }

    return render(request, template, context)
