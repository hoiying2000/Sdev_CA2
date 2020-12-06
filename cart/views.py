from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Item
from .models import Cart, CartItem
from django.conf import settings
from order.models import Order, OrderItem
import stripe

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, item_id):
    item = Item.objects.get(id = item_id)
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
        cart.save()
    try:
        cart_item = CartItem.objects.get(item = item, cart = cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            item = item,
            quantity = 1,
            cart = cart
        )
        cart_item.save()
    return redirect('cart:cart_detail')

def cart_detail(request, total = 0, counter = 0, cart_items = None):
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request))
        cart_items = CartItem.objects.filter(cart = cart, active = True)
        
        for cart_item in cart_items:
            total += (cart_item.item.price * cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass
    stripe.api_key = settings.STRIPE_SECRET_KEY
    stripe_total = int(total * 100)
    data_key = settings.STRIPE_PUBLISHABLE_KEY  
    
    if request.method == 'POST':
        print(request.POST)

        try:
            token = request.POST['stripeToken']
            email =  request.POST['stripeEmail']
            billingName = request.POST['stripeBillingName']
            billingAddress1 = request.POST['stripeBillingAddressLine1']
            billingCity = request.POST['stripeBillingAddressCity']
            billingPostCode = request.POST['stripeBillingAddressZip']
            billingCountry = request.POST['stripeBillingCountryCode']
            shippingName = request.POST['stripeShippingName']
            shippingAddress1 = request.POST['stripeShippingAddressLine1']
            shippingCity = request.POST['stripeShippingAddressCity']
            shippingPostCode = request.POST['stripeShippingAddressZip']
            shippingCountry = request.POST['stripeShippingAddressCountryCode']

            customer = stripe.Customer.create(
                email=email,
                source=token
            )

            charge = stripe.Charge.create(
                    amount=stripe_total,
                    currency="eur",
                    customer=customer.id
                )
            try:
                order_details = Order.objects.create(
                    token = token,
                    total = total,
                    emailAddress = email,
                    billingName = billingName,
                    billingAddress1 = billingAddress1,                    billingCity = billingCity,
                    billingPostCode = billingPostCode,
                    billingCountry = billingCountry,
                    shippingName = shippingName,
                    shippingAddress1 = shippingAddress1,
                    shippingCity = shippingCity,
                    shippingPostCode = shippingPostCode,
                    shippingCountry = shippingCountry
                    )
                order_details.save()
                for order_item in cart_items:
                    oi = OrderItem.objects.create(
                        item = order_item.item.name,
                        quantity = order_item.quantity,
                        price = order_item.item.price,
                        order = order_details
                    )
                    oi.save()

                    items = item.objects.get(id=order_item.item.id)
                    items.stock = int(order_item.item.stock - order_item.quantity)
                    items.save()
                    order_item.delete()
                    print('The order has been made')
                return redirect('order:thanks', order_details.id)
            except ObjectDoesNotExist:
                pass
        except stripe.error.CardError as e:
            return false, e

    return render(request, 'cart.html', {'cart_items':cart_items, 'total':total, 'counter':counter, 'date_key':data_key, 'stripe_total':stripe_total})

def cart_remove(request, item_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    item = get_object_or_404(Item, id = item_id)
    cart_item = CartItem.objects.get(item = item, cart = cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cart_detail')

def full_remove(request, item_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    item = get_object_or_404(Item, id = item_id)
    cart_item = CartItem.objects.get(item = item, cart = cart)
    cart_item.delete()
    return redirect('cart:cart_detail')