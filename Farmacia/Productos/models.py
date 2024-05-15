from django.db import models
from Categorias.models import Categoria
# Create your models here.

class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_en_stock = models.IntegerField()
    fecha_caducidad = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'producto'  #Alias para el modelo
        verbose_name_plural = 'productos'

    def __str__(self):
        return self.nombre