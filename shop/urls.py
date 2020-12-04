from django.urls import path
from .views import ItemListView, ItemDetailView, SearchResultsListView, ItemCreateView, ItemUpdateView, ItemDeleteView

urlpatterns = [
    path('post/delete/', ItemDeleteView.as_view(), name = 'post_delete'),
    path('post/edit/', ItemUpdateView.as_view(), name = 'post_edit'),
    path('post/new/', ItemCreateView.as_view(), name = 'post_new'),
    path('', ItemListView.as_view(), name = 'item_list'),
    path('<uuid:pk>', ItemDetailView.as_view(), name = 'item_detail'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
]
