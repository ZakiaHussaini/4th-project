from django.shortcuts import render, redirect
from product.models import Category, Item


def index(request):
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()

    return render(request, 'index.html', {
        'categories': categories,
        'items': items
    })
    
