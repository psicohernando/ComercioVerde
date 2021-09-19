from django.shortcuts import render
from django.http import HttpResponse

def pagina(request):
    return HttpResponse('Aquí se construye un sueño fresco y verde')