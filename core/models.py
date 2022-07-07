from django.db import models
# Create your models here.

class Articulos(models.Model):
    nombre=models.CharField(max_length=100)
    seccion=models.CharField(max_length=10, null=True, blank=True, verbose_name='Sección')
    precio=models.IntegerField()

    def __str__(self):
        return 'Artículo: %s' % (self.nombre) 
