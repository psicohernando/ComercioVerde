from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from Artesanal.models import *
from Artesanal.serializador import *


def pagina(request):
    return HttpResponse('Aquí se construye un sueño fresco y verde')


class apiartesanias (viewsets.ModelViewSet):
    serializer_class = Serialartesanias
    queryset = Productosartesanal.objects.all()

class apicomentarios (viewsets.ModelViewSet):
    serializer_class = Serialcomentario
    queryset = Comentarios.objects.all()
