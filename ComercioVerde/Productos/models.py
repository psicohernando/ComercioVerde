from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.

class personal(models.Model):
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

    @property
    def numpersonal(self):
        perso = personal.objects.all()
        return len(perso)

class hogar(models.Model):
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

class saludybelleza(models.Model):
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