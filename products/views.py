from django.shortcuts import render
from .models import Product

def all_products(request):
    # Retrieve all products ordered by SKU
    products = Product.objects.order_by('sku')
    return render(request, 'products/all_products.html', {'products': products})


