from django.contrib import admin
from django.urls import path
from comercio.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',vistacomerciox),
    path('ofertas/',oferton)

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 