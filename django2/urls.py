from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from django2 import settings
from products.views import index_page, shop_page, send_form

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page),
    path('shop', shop_page),
    path('form', send_form),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
