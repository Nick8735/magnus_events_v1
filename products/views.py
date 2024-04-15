from django.shortcuts import render
from .models import Product  # Import the Product model

def all_products(request):
    products = Product.objects.all()
    return render(request, 'products/all_products.html', {'products': products})

def wedding_products(request):
    products = Product.objects.filter(category__name='wedding')
    context = {'products': products}
    return render(request, 'products/wedding.html', context)

