from django.core.paginator import Paginator, EmptyPage, InvalidPage
from .models import Item, Category
from django.shortcuts import render, get_object_or_404

def itemCat(request, category_id=None):
    c_page = None
    items_list = None
    if category_id !=None:
        c_page = get_object_or_404(Category, id=category_id)
        items_list = Item.objects.filter(category=c_page, avaliable=True)
    else:
        items_list = Item.objects.all().filter(avaliable=True)

    paginator = Paginator(items_list, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        items = paginator.page(page)
    except (EmptyPage,InvalidPage):
        items = paginator.page(paginator.num_pages)


    return render(request, 'shop/category.html', {'category':c_page, 'items':items})


def item_detail(request, category_id, item_id):
    try:
        item = Item.objects.get(category_id=category_id, id=item_id)
    except Exception as e:
        raise e
    return render(request, 'shop/item.html', {'item':item})


