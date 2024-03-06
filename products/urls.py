from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),  # This should match the URL 'products/'
    path('wedding/', views.wedding_products, name='wedding'),  # Assuming you have a view for wedding products
    # Add more URL patterns as needed
]
