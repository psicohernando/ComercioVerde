from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework import exceptions, serializers
from Artesanal.models import *

class Serialcomentario(serializers.ModelSerializer):
    class Meta:
        model = Comentarios
        fields = '__all__'

class Serialcategoria(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class Serialartesanias(serializers.ModelSerializer):
    class Meta:
        model = Productosartesanal
        fields = '__all__'
