from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    # Assuming you have a view for wedding within the home app
    path('wedding/', views.wedding_view, name='wedding'),
    # Add more URL patterns as needed
]
