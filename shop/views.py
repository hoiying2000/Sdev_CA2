from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Item


class ItemListView(ListView):
    model = Item
    context_object_name = 'item_list'
    template_name = 'items/item_list.html'


class ItemDetailView(DetailView):
    model = Item
    context_object_name = 'item'
    template_name = 'items/item_detail.html'

class SearchResultsListView(ListView):
    model = Item
    context_object_name = 'item_list'
    template_name = 'items/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Item.objects.filter(
            Q(title__icontains=query) | Q(title__icontains=query)
        )

class ItemCreateView(CreateView):
    model = Item
    fields = ('cover', 'title', 'brand', 'price')
    template_name = 'post_new.html'


class ItemUpdateView(UpdateView):
    model = Item
    fields = ('cover', 'title', 'brand', 'price')
    template_name = 'post_edit.html'


class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')