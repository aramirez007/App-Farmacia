from django import forms
from .models import Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'decripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe la categoria'}),
            'decripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe la descripción'}),
        }