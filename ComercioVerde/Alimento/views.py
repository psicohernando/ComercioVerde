from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from Alimento.models import *
from Alimento.serializador import *


def pagina(request):
    return HttpResponse('Aquí se construye un sueño fresco y verde')


class apialimento (viewsets.ModelViewSet):
    serializer_class = Serialalimento
    queryset = Alimentos.objects.all()