from django.contrib import admin
from django.urls import path
from Ventas.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',pagina),
    path('Compras/',pagina),
    path('Items/',pagina),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 