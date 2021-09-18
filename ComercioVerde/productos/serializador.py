from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework import exceptions, serializers
from Productos.models import *

class Serialpersonal(serializers.ModelSerializer):
    class Meta:
        model = personal
        fields = ['Nombre','Precio','Descripcion','Foto','numpersonal']

class Serialhogar(serializers.ModelSerializer):
    class Meta:
        model = hogar
        fields = '__all__'

class Serialsaludybelleza(serializers.ModelSerializer):
    class Meta:
        model = saludybelleza
        fields = '__all__'