from django.contrib import admin
<<<<<<< HEAD
from django.urls import path
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from comercio.views import vistacomerciox

urlpatterns = [
    path('principal/', admin.site.urls),
    path('fresco/',include('comercio.urls')),
    path('',vistacomerciox)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
=======
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('principal', admin.site.urls),
    path('fresco/',include('comercio.urls')),
    path('chek/',include('Checkout.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 09000cce4ff81a7d9a4bd6d28a0c55388595946b
