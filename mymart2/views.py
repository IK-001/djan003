from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')

def order_history(request):
    return render(request, 'order_history.html')

def logout_user(request):
    logout(request)
    return redirect('home')

def cart_detail(request):
    # Your logic to retrieve cart items and total price goes here
    cart_items = []
    total_price = 0
    return render(request, 'cart_detail.html', {'cart_items': cart_items, 'total_price': total_price})
