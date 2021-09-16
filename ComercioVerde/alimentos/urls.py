from django.contrib import admin
from django.urls import path,include
from Alimentos.views import *
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter

##router = DefaultRouter()
##outer.register('verduras',pagina)

urlpatterns = [
    path('',pagina),
    path('alimento/',pagina),
    path('frutas/',pagina),
    path('verduras/',pagina),
    path('postres/',pagina),
    path('vegano/',pagina),
    ##path('api/',include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 