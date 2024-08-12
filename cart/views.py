from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from products.models import Product
from django.contrib.auth.models import User

@login_required
def cart_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart:cart_detail')

@login_required
def cart_remove(request, product_id):
    cart = Cart.objects.get(user=request.user)
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(cart=cart, product=product)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cart_detail')

@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart/cart.html', {'cart': cart})

@login_required
def checkout_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = sum([item.product.price * item.quantity for item in cart_items])
    if request.method == 'POST':
        # Process the payment and clear the cart
        # For now, just clear the cart
        cart_items.delete()
        return redirect('products:product_list')
    return render(request, 'cart/checkout.html', {'cart': cart, 'total_price': total_price})