<<<<<<< HEAD
from comercio.models import Productos_Organicos
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

# Create your views here.
def vistacomerciox(request):
    return render(request,'comercio/inicio.html')

def vistaproductos(request):
    product = Productos_Organicos.objects.all()
    return render(request, 'comercio/productos.html', {'product:': product})
=======
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def vistacomerciox(request):
    return HttpResponse('Bienvenido a fresco. El lugar más fresco para la canasta familiar')

def vistaproductos(request):
    return HttpResponse('Productos fresco: ¿Qué desea llevar?')
>>>>>>> 09000cce4ff81a7d9a4bd6d28a0c55388595946b

def vistaalimentos(request):
    return HttpResponse('Alimentos fresco: ¿Cómo te quieres alimentar?')

def vistaartesanias(request):
    return HttpResponse('Artesanías fresco: ¿Que deseas llevar?')

def oferton(request):
<<<<<<< HEAD
    return HttpResponse('esto es una pagina de ofertas')

def pagina(request):
    return HttpResponse('Aquí se construye un sueño fresco y verde')
=======
    return HttpResponse('esto es ña pagina de ofertas')
>>>>>>> 09000cce4ff81a7d9a4bd6d28a0c55388595946b
