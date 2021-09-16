from django.db import models
from django.db.models.fields.related import ForeignKey

class Artesanias(models.Model):
    Nombre=models.CharField(max_length=100,null=True,blank=True)
    Precio=models.FloatField(max_length=7,null=True,blank=True)
    Descripcion=models.CharField(max_length=500,null=True, blank=True)
    Foto=models.ImageField(upload_to='artesania',null=True,blank=True)

    def __str__(self):
        return self.Nombre

class Ropa(models.Model):
    Nombre=models.CharField(max_length=100,null=True,blank=True)
    Precio=models.FloatField(max_length=7,null=True,blank=True)
    Talla=models.CharField(max_length=100,null=True,blank=True)
    Descripcion=models.CharField(max_length=500,null=True, blank=True)
    Foto=models.ImageField(upload_to='artesania',null=True,blank=True)

    def __str__(self):
        return self.Nombre

class Otros(models.Model):
    Nombre=models.CharField(max_length=100,null=True,blank=True)
    Precio=models.FloatField(max_length=7,null=True,blank=True)
    Descripcion=models.CharField(max_length=500,null=True, blank=True)
    Foto=models.ImageField(upload_to='artesania',null=True,blank=True)

    def __str__(self):
        return self.Nombre