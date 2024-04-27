from django.shortcuts import render, get_object_or_404
from .models import Product

def all_products(request):
    # Retrieve all products ordered by SKU
    products = Product.objects.order_by('sku')

    context = {
        'products': products,
    }
    return render(request, 'products/all_products.html', {'products': products})

def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'products': products,
    }

    return render(request, 'products/product_detail.html', context)
