from django.db import models
from django.contrib.auth.models import User
from Productos.models import Productos

# Create your models here.
class Venta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_venta = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'venta'  #Alias para el modelo
        verbose_name_plural = 'ventas'

    def __str__(self):
        return f'Creada por: { self.usuario} - el: ' + self.fecha_venta.strftime('%d-%m-%Y')


class DetalleVenta(models.Model):
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'detalle_venta'  #Alias para el modelo
        verbose_name_plural = 'detalle_ventas'


class Ventas(models.Model):
    id = models.IntegerField(primary_key=True)
    fecha_venta = models.DateField()
    username = models.CharField(max_length=100)
    total = models.FloatField()

    class Meta:
        managed = False
        db_table = 'ventas'