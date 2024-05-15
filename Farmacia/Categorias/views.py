from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria
from .forms import CategoriaForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse

# Create your views here.
@login_required
def categorias(request):
    categorias_lista = Categoria.objects.all().order_by('nombre')
    form = CategoriaForm()

    pagina = Paginator(categorias_lista, 10)
    pagina_n = request.GET.get('page')
    categorias = pagina.get_page(pagina_n)
    return render(request, "Categorias.html", {"categorias": categorias, "form": form})


@login_required
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('categorias')
        
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    
    else:
        form = CategoriaForm()
    return render(request, "Categorias.html", {"form": form})


@login_required
def eliminar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)

    if request.method == 'GET':
        categoria.delete()
        return redirect('categorias')
    

@login_required
def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)

    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)

        if form.is_valid():
            form.save()
            return redirect('categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, "detalle_categoria.html", {"form": form, 'categoria': categoria})