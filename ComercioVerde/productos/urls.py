from django.contrib import admin
from django.urls import path
from Productos.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',pagina),
    path('personal/',pagina),
    path('hogar/',pagina),
    path('saludybelleza/',pagina),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 