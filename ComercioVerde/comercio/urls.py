from django.contrib import admin
from django.urls import path
from comercio.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', LandingPage.as_view()),
    path("productos", productos.as_view()),
    path("blog", blog.as_view()),
    path("contactanos", single.as_view()),
    path("alimentos", alimentov.as_view()),
    path("artesanias", artesaniasv.as_view()),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 