from django.shortcuts import render
from .models import Products


def all_products(request):
    """ view to show all products, sorting and searching """

    products = Product.object.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
