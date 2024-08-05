from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def profile(request):
    # Assuming you have a template for the profile page
    return render(request, 'accounts/profile.html')

@login_required
def order_history(request):
    # You can add logic here to retrieve and display the user's order history
    orders = []  # Replace with actual data retrieval logic
    return render(request, 'accounts/order_history.html', {'orders': orders})
