from django.shortcuts import render, get_object_or_404
from .models import Product

def all_products(request):
    # Retrieve all products ordered by SKU
    products = Product.objects.order_by('sku')

    context = {
        'products': products,
    }
    return render(request, 'products/all_products.html', context)

def product_detail(request, product_id):
    """ A view to show individual product details """

    # Retrieve a specific product by its ID (product_id)
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,  # Use 'product' instead of 'products' here
    }

    return render(request, 'products/product_detail.html', context)

