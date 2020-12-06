from django.contrib import admin
from .models import Order, OrderItem

 
class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    fieldsets = [
        ('Item', {'fields': ['item'],}),
        ('Quantity',{'fields': ['quantity'],}),
        ('Price', {'fields': ['price'],}),
    ]
    readonly_fields = ['item', 'quantity', 'price']
    can_delete=False
    max_num = 0
    template = 'admin/order/tabular.html'

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'billingName', 'emailAddress', 'created']
    list_display_links = ('id', 'billingName')
    search_fields = ['id', 'billingName', 'emailAddress']
    readonly_fields = ['id', 'token', 'emailAddress', 'created', 'billingName', 'billingAddress1', 'billingCity', 'billingPostCode', 'billingCountry', 'shippingName', 'shippingAddress1', 'shippingCity', 'shippingPostCode', 'shippingCountry']
    fieldsets = [
        ('ORDER INFORMATION', {'fields': ['id', 'token', 'total', 'created']}),
        ('BILLING INFORMATION', {'fields': ['billingName', 'billingAddress1', 'billingCity', 'billingPostCode', 'billingCountry', 'emailAddress']}),
        ('SHIPPING INFORMATION', {'fields': ['ahippingName', 'shippingAddress1', 'shippingCity', 'shippingPostCode', 'shippingCountry']}),
    ]

    inlines = [
        OrderItemAdmin,
    ]

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

admin.site.register(Order, OrderAdmin)