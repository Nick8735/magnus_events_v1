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
    items = Item.objects.filter(category='wedding')
    print(items)  # Add this line to print items
    context = {'items': items}
    return render(request, 'products/wedding.html', context)

