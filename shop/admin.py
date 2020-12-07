from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ("title", "brand", "price", "cover",)

admin.site.register(Item, ItemAdmin)