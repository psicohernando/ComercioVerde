class comentario:
    def __init__(self,email,contenido,fecha=None):
        self.email=email
        self.contenido=contenido
        self.fecha=fecha

from rest_framework import serializers

class comenser(serializers.Serializer):
    email=serializers.EmailField()
    contenido=serializers.CharField()
    fecha=serializers.DateField()

com1=comentario('jaja','kakakakak')
print(com1.email)


prueba=comenser(com1)
print(prueba.data)

#----------------------------------------

