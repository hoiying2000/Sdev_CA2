from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.itemCat, name = 'itemCat'),
    path('<uuid:category_id>/', views.itemCat, name='items_by_category'),
    path('<uuid:category_id>/<uuid:item_id>/', views.item_detail, name='item_detail'),
]
