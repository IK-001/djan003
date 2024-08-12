# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
# from products import views as product_views  # Import the home view

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('products.urls')),
#     path('', product_views.home, name='home'),  # Set the home URL pattern
#     path('cart/', include('cart.urls')),
#     path('accounts/', include('accounts.urls')),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



from django.urls import path, include
from .views import home, profile, order_history, logout_user
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf import settings
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('profile/', profile, name='profile'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('order_history/', order_history, name='order_history'),
    path('logout/', logout_user, name='logout'),
    # path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/', include('cart.urls', namespace='cart')),
    path('products/', include('products.urls', namespace='products')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]