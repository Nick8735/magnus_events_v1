# products/views.py

from django.shortcuts import render
from django.http import HttpResponse

def all_products(request):
    # Your logic to display all products
    return HttpResponse("All Products")

def wedding_products(request):
    # Your logic to display wedding products
    # Assuming you have a template named 'wedding.html' in the 'products' app's 'templates' directory
    return render(request, 'home/wedding.html')