from django.db import models
from django.db.models.fields.related import ForeignKey
from Alimentos.models import *
from Productos.models import *
from Artesanal.models import *

class Carritocompras(models.Model):
    usuario=models.CharField(max_length=100,null=True,blank=True)
    fecha=models.DateField(auto_now_add=True,null=True,blank=True)
  
    def __str__(self):
        return self.usuario

    def total(self):
        pass

class Items(models.Model):
    Verduras=models.ManyToManyField(verduras)
    Frutas=models.ManyToManyField(frutas)
    Postres=models.ManyToManyField(postres)
    alimentos=models.ManyToManyField(alimento)
    veganos=models.ManyToManyField(vegano)

    artesanias=models.ManyToManyField(Artesanias)
    ropa=models.ManyToManyField(Ropa)
    otros=models.ManyToManyField(Otros)

    Personal=models.ManyToManyField(personal)
    Hogar=models.ManyToManyField(hogar)
    Salud=models.ManyToManyField(saludybelleza)


    carrito=models.ForeignKey(Carritocompras,on_delete=models.CASCADE)

    def suma(Items):
        pass
    
