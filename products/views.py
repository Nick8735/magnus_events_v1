from django.shortcuts import render
from .models import Product

def all_products(request):
    # Retrieve all products
    products = Product.objects.all()
    return render(request, 'products/all_products.html', {'products': products})

def wedding_products(request):
    # Filter products by category
    products_w1 = Product.objects.filter(category__friendly_name='W1')
    products_w2 = Product.objects.filter(category__friendly_name='W2')
    products_w3 = Product.objects.filter(category__friendly_name='W3')
    
    # Create a dictionary to hold products for each category
    categories = {'W1': products_w1, 'W2': products_w2, 'W3': products_w3}
    
    return render(request, 'products/wedding_products.html', {'categories': categories})
