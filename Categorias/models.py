from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    decripcion = models.TextField()

    class Meta:
        verbose_name = 'categoria'  #Alias para el modelo
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nombre