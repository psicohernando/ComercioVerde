from django.db import models

# Create your models here.

from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here. aquí va el crud


class verduras(models.Model):
    Nombre=models.CharField(max_length=100, null=True, blank=True)
    Precio=models.FloatField(max_length=7,null=True,blank=True)
    Unidad=models.CharField(max_length=100, null=True, blank=True)
    Cantidad=models.FloatField(max_length=100, null=True, blank=True)
    Foto=models.ImageField(upload_to='alimento',null=True,blank=True)
    Fechaelaboracion=models.DateField(null=True,blank=True)
    Fechavencimiento=models.DateField(null=True,blank=True)

    def __str__(self):
        return self.Nombre

class frutas(models.Model):
    Nombre=models.CharField(max_length=100, null=True, blank=True)
    Precio=models.FloatField(max_length=7,null=True,blank=True)
    Unidad=models.CharField(max_length=100, null=True, blank=True)
    Cantidad=models.FloatField(max_length=100, null=True, blank=True)
    Foto=models.ImageField(upload_to='alimento',null=True,blank=True)
    Fechaelaboracion=models.DateField(null=True,blank=True)
    Fechavencimiento=models.DateField(null=True,blank=True)

    def __str__(self):
        return self.Nombre

class vegano(models.Model):
    Nombre=models.CharField(max_length=100, null=True, blank=True)
    Precio=models.FloatField(max_length=7,null=True,blank=True)
    Unidad=models.CharField(max_length=100, null=True, blank=True)
    Cantidad=models.FloatField(max_length=100, null=True, blank=True)
    Foto=models.ImageField(upload_to='alimento',null=True,blank=True)
    Fechaelaboracion=models.DateField(null=True,blank=True)
    Fechavencimiento=models.DateField(null=True,blank=True)

    def __str__(self):
        return self.Nombre

class postres(models.Model):
    Nombre=models.CharField(max_length=100, null=True, blank=True)
    Precio=models.FloatField(max_length=7,null=True,blank=True)
    Unidad=models.CharField(max_length=100, null=True, blank=True)
    Cantidad=models.FloatField(max_length=100, null=True, blank=True)
    Foto=models.ImageField(upload_to='alimento',null=True,blank=True)
    Fechaelaboracion=models.DateField(null=True,blank=True)
    Fechavencimiento=models.DateField(null=True,blank=True)

    def __str__(self):
        return self.Nombre

class alimento(models.Model):
    Nombre=models.CharField(max_length=100, null=True, blank=True)
    Precio=models.FloatField(max_length=7,null=True,blank=True)
    Unidad=models.CharField(max_length=100, null=True, blank=True)
    Cantidad=models.FloatField(max_length=100, null=True, blank=True)
    Foto=models.ImageField(upload_to='alimento',null=True,blank=True)
    Fechaelaboracion=models.DateField(null=True,blank=True)
    Fechavencimiento=models.DateField(null=True,blank=True)

    def __str__(self):
        return self.Nombre