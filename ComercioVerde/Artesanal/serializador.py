from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework import exceptions, serializers
from Artesanal.models import *

class Serialartesanias(serializers.ModelSerializer):
    class Meta:
        model = Artesanias
        fields = '__all__'

class Serialropa(serializers.ModelSerializer):
    class Meta:
        model = Ropa
        fields = '__all__'

class Serialotros(serializers.ModelSerializer):
    class Meta:
        model = Otros
        fields = '__all__'
