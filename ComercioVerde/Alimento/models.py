from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

class Categoria(models.Model):
    categoria = models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.categoria

class Alimentos(models.Model):
    categoria = models.ForeignKey(Categoria,on_delete=CASCADE)
    Nombre=models.CharField(max_length=100, null=True, blank=True)
    Precio=models.FloatField(max_length=7,null=True,blank=True)
    Descripcion=models.CharField(max_length=500, null=True, blank=True)
    Unidad=models.CharField(max_length=100, null=True, blank=True)
    Cantidad=models.FloatField(max_length=100, null=True, blank=True)
    Foto=models.ImageField(upload_to='producto',null=True,blank=True)
    Fechaelaboracion=models.DateField(null=True,blank=True)
    Fechavencimiento=models.DateField(null=True,blank=True)
    def __str__(self):
        return self.Nombre