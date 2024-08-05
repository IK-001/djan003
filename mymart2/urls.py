from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from products import views as product_views  # Import the home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('', product_views.home, name='home'),  # Set the home URL pattern
    path('cart/', include('cart.urls')),
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
