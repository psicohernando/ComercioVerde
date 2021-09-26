from django.db import models
from django.db.models.fields.related import ForeignKey

class Categoria(models.Model):
    categoria = models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.categoria

class Productosartesanal(models.Model):
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    Nombre=models.CharField(max_length=100)
    Precio=models.FloatField(max_length=7)
    Descripcion=models.CharField(max_length=500, null=True, blank=True)
    stock=models.FloatField()
    Foto=models.ImageField(upload_to='producto',null=True,blank=True)
    descuento = models.FloatField()
    Lugarelaboracion = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Nombre

class Comentarios(models.Model):
    usuario = models.CharField(max_length=500, null=True, blank=True)
    comentario = models.CharField(max_length=500, null=True, blank=True)
    productos = models.ForeignKey(Productosartesanal,on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.productos.__str__() + '  /  ' + self.fecha.__str__()
