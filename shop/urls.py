from django.urls import path
from .views import ItemListView, ItemDetailView, SearchResultsListView

urlpatterns = [
    path('', ItemListView.as_view(), name = 'item_list'),
    path('<uuid:pk>', ItemDetailView.as_view(), name = 'item_detail'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
]
