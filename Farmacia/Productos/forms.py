from django import forms
from .models import Productos

class ProductosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['nombre', 'descripcion', 'precio', 
                  'cantidad_en_stock', 'fecha_caducidad', 'categoria']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el nombre del producto'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa la descripción'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el precio'}),
            'cantidad_en_stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad en Stock'}),
            'fecha_caducidad': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'categoria': forms.SelectMultiple(attrs={'class': 'form-control dropdown'}),
        }