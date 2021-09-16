from django.contrib import admin
from django.urls import path
from comercio.views import *
from django.conf import settings
from django.conf.urls.static import static

<<<<<<< HEAD

=======
>>>>>>> 09000cce4ff81a7d9a4bd6d28a0c55388595946b
urlpatterns = [
    path('',vistacomerciox),
    path('productos/',vistaproductos),
    path('alimentos/',vistaalimentos),
    path('artesanias/',vistaartesanias),
    path('ofertas/',oferton)
<<<<<<< HEAD

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
=======
        
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 09000cce4ff81a7d9a4bd6d28a0c55388595946b
