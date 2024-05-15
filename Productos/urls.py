from django.urls import path
from Productos import views

urlpatterns = [
    path('', views.productos, name='productos'),
    path('crear_producto/', views.crear_producto, name='crear_producto'),
    path('eliminar_producto/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('editar_producto/<int:producto_id>/', views.editar_producto, name='editar_producto'),
]