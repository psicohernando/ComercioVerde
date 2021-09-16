from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework import exceptions, serializers
from Ventas.models import *

class Serialcarro(serializers.ModelSerializer):
    class Meta:
        model = Carritocompras
        fields = '__all__'

class Serialitems(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'