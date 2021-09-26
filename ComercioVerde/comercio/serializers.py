#convierte python en json y viceversa.

from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework import exceptions, serializers
from comercio.models import *


class SerAlimentos(serializers.Serializer):
    NombreAlimento=serializers.CharField()
    PrecioAlimento=serializers.FloatField()
    UnidadAlimento=serializers.CharField()
    CantidadAlimento=serializers.FloatField()
    FechaelaboracionAl=serializers.DateField()
    FechavencimientoAl=serializers.DateField()

class Ser2Alimento(serializers.ModelSerializer):
    class Meta:
        model = Alimentos
        fields = '__all__'
        fields = ['NombreAlimento','PrecioAlimento','CantidadAlimento',]
        ##exceptions = ['FechavencimientoAl']

class Ser3Alimento(serializers.ModelSerializer):
    class Meta:
        model = Alimentos
        fields = ['NombreAlimento','PrecioAlimento','numal']
