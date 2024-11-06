from django.shortcuts import render, redirect
from . models import Order, OrderedItem
from products.models import Product
from customers.models import Customer
# Cart
def show_cart(request):
    user = request.user
    customer = user.customer_profile
    cart_obj, created = Order.objects.get_or_create(
             owner = customer,
             order_status = Order.CART_STAGE
        )
    context = {
        'cart': cart_obj
    }
    
    return render(request, 'cart.html', context)

# Add to Cart
def add_to_cart(request):
    if request.POST and request.user.is_authenticated:
        user = request.user
        customer = user.customer_profile
        quantity = int(request.POST.get('quantity', 1))
        size = request.POST.get('size')
        product_id = request.POST.get('product_id')
        cart_obj, created = Order.objects.get_or_create(
             owner = customer,
             order_status = Order.CART_STAGE
        )
        product = Product.objects.get(pk = product_id)
        ordered_item,created = OrderedItem.objects.get_or_create(
            product = product,
            owner = cart_obj,
            quantity = quantity,
            size = size,
        )
        if created:
            ordered_item.quantity = quantity
            ordered_item.save()
        else:
            ordered_item.quantity = ordered_item.quantity + quantity
            ordered_item.save()
            
        return redirect('cart')
    else:
        return redirect('login')
