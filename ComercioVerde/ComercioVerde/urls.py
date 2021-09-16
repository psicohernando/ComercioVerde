from django.contrib import admin
from django.urls import path
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from comercio.views import vistacomerciox

urlpatterns = [
    path('principal/', admin.site.urls),
    path('fresco/',include('comercio.urls')),
    path('',vistacomerciox),
    path('Alimentos/',include('Alimentos.urls')),
    path('Artesanal/',include('Artesanal.urls')),
    path('Productos/',include('Productos.urls')),
    path('Compras/',include('Ventas.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 