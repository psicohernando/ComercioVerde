from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework import exceptions, serializers
from Alimentos.models import *

class Serialalimento(serializers.ModelSerializer):
    class Meta:
        model = alimento
        fields = '__all__'

class Serialverduras(serializers.ModelSerializer):
    class Meta:
        model = verduras
        fields = '__all__'

class Serialpostres(serializers.ModelSerializer):
    class Meta:
        model = postres
        fields = '__all__'

class Serialfrutas(serializers.ModelSerializer):
    class Meta:
        model = frutas
        fields = '__all__'

class Serialvegano(serializers.ModelSerializer):
    class Meta:
        model = vegano
        fields = '__all__'

