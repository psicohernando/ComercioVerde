from django.db import models

# Create your models here.

class Carrito(models.Model):
    descuento = models.FloatField(default=0)
    usuarios=models.CharField(max_length=100)
    total=0
    listacompra={}

class productoscom(models.Model):

    opciones=(
        ("Mujer","m"),
        ("Hombre","h")
    )

    nombre = models.CharField(max_length=100)
    precio = models.FloatField(default=0)
    categoria = models.CharField(max_length=100,choices=opciones)
    cod_barras=models.CharField(max_length=100,primary_key=True)


class Items(models.Model):
    producto= models.ForeignKey(productoscom,on_delete=models.CASCADE)
    cantidad=models.IntegerField(default=0)
    carrito=models.ForeignKey(Carrito,on_delete=models.CASCADE)