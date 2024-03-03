from django.contrib import admin
from django.urls import path
from home.views import index, wedding_view

urlpatterns = [
    path('', index, name='home'),
    path('wedding/', wedding_view, name='wedding'),
]
