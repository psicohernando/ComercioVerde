from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from Alimentos.models import *
from Alimentos.serializador import *


def pagina(request):
    return HttpResponse('Aquí se construye un sueño fresco y verde')


class apialimento (viewsets.ModelViewSet):
    serializer_class = Serialalimento
    queryset = alimento.objects.all()


class apiverduras (viewsets.ModelViewSet):
    serializer_class = Serialverduras
    queryset = verduras.objects.all()

class apifrutas (viewsets.ModelViewSet):
    serializer_class = Serialfrutas
    queryset = frutas.objects.all()

class apivegano (viewsets.ModelViewSet):
    serializer_class = Serialvegano
    queryset = vegano.objects.all()

class apipostres (viewsets.ModelViewSet):
    serializer_class = Serialpostres
    queryset = postres.objects.all()