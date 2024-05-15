from django.urls import path
from Ventas import views

urlpatterns = [
    path('', views.ventas, name='ventas'),
    path('crear_venta/', views.crear_venta, name='crear_venta'),
]