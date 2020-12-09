from django.shortcuts import render
from shop.models import Item
from django.db.models import Q

def searchResults(request):
    items = None
    query = None
    if 'q' in request.GET:
        query =  request.GET.get('q')
        items = Item.objects.all().filter(Q(title__contains=query) | Q(brand__contains=query))
    return render(request, 'search.html', {'query':query, 'items':items})
