from comercio.models import Productos_Organicos
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

# Create your views here.
def vistacomerciox(request):
    return render(request,'comercio/index.html')

def vistaproductos(request):
    product = Productos_Organicos.objects.all()
    return render(request, 'comercio/productos.html', {'product:': product})

def vistaalimentos(request):
    return HttpResponse('Alimentos fresco: ¿Cómo te quieres alimentar?')

def vistaartesanias(request):
    return HttpResponse('Artesanías fresco: ¿Que deseas llevar?')

def oferton(request):
    return HttpResponse('esto es una pagina de ofertas')

def pagina(request):
    return HttpResponse('Aquí se construye un sueño fresco y verde')