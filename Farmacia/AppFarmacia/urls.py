from django.urls import path
from AppFarmacia import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
]