from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from Productos.models import Productos
from .models import Venta, DetalleVenta, Ventas
import json
from django.core.paginator import Paginator

# Create your views here.

@login_required
def ventas(request):
    ventas_lista = Ventas.objects.all().order_by('-fecha_venta')

    pagina = Paginator(ventas_lista, 10)
    pagina_n = request.GET.get('page')
    ventas = pagina.get_page(pagina_n)
    return render(request, "ventas.html", {"ventas": ventas})

@login_required
def crear_venta(request):

    if request.method == 'POST':
        general = json.loads(request.body)

        total = general.get("total")        
        detalles = general.get("datos")

        venta = Venta(usuario=request.user, total=total)
        venta.save()

        for detalle in detalles:
            producto = detalle.get("producto")
            cantidad = detalle.get("cantidad")
            precio = detalle.get("precio_unitario")

            producto = Productos.objects.get(nombre=producto)

            detalle_venta = DetalleVenta(producto=producto, venta=venta, cantidad=cantidad, precio_unitario=precio)
            detalle_venta.save()

        return redirect('ventas')

    else:
        productoscarro = Productos.objects.all()
    
    return render(request, "crear_venta.html", {"productoscarro": productoscarro})