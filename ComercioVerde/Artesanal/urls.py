from django.contrib import admin
from django.urls import path,include
from Artesanal.views import *
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('artesania',apiartesanias)
router.register('ropa',apiropa)
router.register('otros',apiotros)


urlpatterns = [
    path('',pagina),
    path('crud/',include(router.urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 