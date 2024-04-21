from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),  # This should match the URL 'products/'
  
    # Add more URL patterns as needed
]
