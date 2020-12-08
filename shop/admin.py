from django.contrib import admin
from .models import Item, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category, CategoryAdmin)

class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'brand', 'price', 'cover','category' , 'stock', 'avaliable', 'stock', 'avaliable', ]
    list_editable = ['price', 'stock', 'avaliable']
    list_per_page = 20
admin.site.register(Item, ItemAdmin)