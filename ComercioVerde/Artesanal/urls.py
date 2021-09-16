from django.contrib import admin
from django.urls import path
from Artesanal.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',pagina),
    path('artesania/',pagina),
    path('ropa/',pagina),
    path('otros/',pagina),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 