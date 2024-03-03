from django.shortcuts import render
from .models import Item

def get_wedding_list(request):
    items = Item.objects.filter(category='wedding category')
    context = {
        'items': items
    }
    return render(request, 'home/wedding.html', context)
