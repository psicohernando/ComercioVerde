from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework import exceptions, serializers
from Productos.models import *

class Serialpersonal(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = ['Nombre','Precio','Descripcion','Foto','numpersonal']