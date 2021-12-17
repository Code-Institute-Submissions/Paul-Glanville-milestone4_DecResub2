from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('products/', include('products.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    #path('reviews/', include('reviews.urls')),
    #path('wishlist/', include('wishlist.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
