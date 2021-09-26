from django.db import models
from django.contrib.auth import get_user_model

class Perfil (models.Model):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    nombres_apellido_RS = models.CharField(max_length=200)
    cc = models.BooleanField()
    nit = models.BooleanField()
    numidentificacion = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    departamento = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)


    def _str_(self):
        return self.usuario.username

