from django.urls import path
from Categorias import views

urlpatterns = [
    path('', views.categorias, name='categorias'),
    path('crear_categoria/', views.crear_categoria, name='crear_categoria'),
    path('eliminar_categoria/<int:categoria_id>/', views.eliminar_categoria, name='eliminar_categoria'),
    path('editar_categoria/<int:categoria_id>/', views.editar_categoria, name='editar_categoria'),
]