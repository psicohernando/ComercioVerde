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
    path('productosapi/',include('Productos.urls')),
    path('artesanalapi/',include('Artesanal.urls')),
    path('alimentosapi/',include('Alimento.urls')),
    path('usuarios/api/', include('Usuarios.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 