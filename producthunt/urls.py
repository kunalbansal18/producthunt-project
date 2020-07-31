from django.contrib import admin
from django.urls import path, include
from productsapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage, name = 'home'),
    path('accounts/',include('accountsapp.urls')),
    path('products/',include('productsapp.urls')),
    ] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
