from django.shortcuts import render
from .models import Item

def index(request):
    # Your index view logic here
    items = Item.objects.all()  # Example query to retrieve items
    context = {
        'items': items
    }
    return render(request, 'home/index.html', context)

def wedding_view(request):
    # Your wedding view logic here
    items = Item.objects.filter(category='wedding')  # Example query to retrieve wedding items
    context = {
        'items': items
    }
    return render(request, 'home/wedding.html', context)
