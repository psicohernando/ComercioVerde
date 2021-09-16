from django.db import models

# Create your models here.
class Artesanias(models.Model):
    NombreArtesania=models.CharField(max_length=100,null=True,blank=True)
    PrecioArtesania=models.FloatField(max_length=7,null=True,blank=True)
    DescripcionArtesania=models.CharField(max_length=500, null=True, blank=True)
    FotoArtesania=models.ImageField(upload_to='artesania',null=True,blank=True)

    def __str__(self):
        return self.NombreArtesania