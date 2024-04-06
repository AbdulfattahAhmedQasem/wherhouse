
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('account/',include('account.urls')),
    path('orders/',include('orders.urls')),
    path('',include('product.urls')),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
