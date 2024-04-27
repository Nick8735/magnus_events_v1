from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),  # This should match the URL 'products/'
    path('<product_id>', views.product_detail, name='product_detail'),
    # Add more URL patterns as needed
]
