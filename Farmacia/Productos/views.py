from django.shortcuts import render, redirect, get_object_or_404
from .models import Productos
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import ProductosForm

# Create your views here.

@login_required
def productos(request):
    productos_lista = Productos.objects.all().order_by('nombre')
    form = ProductosForm()

    pagina = Paginator(productos_lista, 10)
    pagina_n = request.GET.get('page')
    productos = pagina.get_page(pagina_n)
    return render(request, "Productos.html", {"productos": productos, "form": form})


@login_required
def crear_producto(request):
    if request.method == 'POST':
        form = ProductosForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('productos')
    
    else:
        form = ProductosForm()
    return render(request, "Productos.html", {"form": form})


@login_required
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Productos, pk=producto_id)

    if request.method == 'GET':
        producto.delete()
        return redirect('productos')
    

@login_required
def editar_producto(request, producto_id):
    producto = get_object_or_404(Productos, pk=producto_id)

    if request.method == 'POST':
        form = ProductosForm(request.POST, instance=producto)

        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = ProductosForm(instance=producto)

    return render(request, "detalle_producto.html", {"form": form, "producto": producto})