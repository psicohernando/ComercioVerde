from django.db.models.query import QuerySet
from django.http.request import QueryDict
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.serializers import SerializerMetaclass

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response

from Alimentos.serializador import *

def pagina(request):
    return HttpResponse('Aquí se construye un sueño fresco y verde')

