from django.shortcuts import render
from .models import Product

def all_products(request):
    products_w1 = Product.objects.filter(category__friendly_name='W1')
    products_w2 = Product.objects.filter(category__friendly_name='W2')
    products = Product.objects.all()
    return render(request, 'products/all_products.html', {'products': products})

def wedding_products(request):
    products_w1 = Product.objects.filter(category__friendly_name='W1')
    products_w2 = Product.objects.filter(category__friendly_name='W2')
    categories = {'W1': products_w1, 'W2': products_w2}
    return render(request, 'products/all_products.html', {'categories': categories})
