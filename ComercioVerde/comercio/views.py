from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def vistacomerciox(request):
    return HttpResponse('Bienvenido a fresco. El lugar más fresco para la canasta familiar')

def vistaproductos(request):
    return HttpResponse('Productos fresco: ¿Qué desea llevar?')

def vistaalimentos(request):
    return HttpResponse('Alimentos fresco: ¿Cómo te quieres alimentar?')

def vistaartesanias(request):
    return HttpResponse('Artesanías fresco: ¿Que deseas llevar?')

def oferton(request):
    return HttpResponse('esto es ña pagina de ofertas')