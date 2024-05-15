from django.urls import path
from Autenticacion import views

urlpatterns = [
    path('', views.iniciar_sesion, name='login'),
    path('autenticacion/', views.VRegistro.as_view(), name='Autenticacion'),
    path('cerrar_sesion', views.cerrar_sesion, name='logout')
]