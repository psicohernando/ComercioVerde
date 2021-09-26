from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework import exceptions, serializers
from Alimento.models import *

class Serialalimento(serializers.ModelSerializer):
    class Meta:
        model = Alimentos
        fields = '__all__'

#class Serialalimento(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = Alimentos
#        fields = '__all__'
#crear serilizador de la clase categoria