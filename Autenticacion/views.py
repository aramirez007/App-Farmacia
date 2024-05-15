from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

class VRegistro(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "registro.html", {"form": form})
    
    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("login")
        
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, "registro.html", {"form": form})
        

def iniciar_sesion(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.cleaned_data.get("username")
            passwd = form.cleaned_data.get("password")
            usuario = authenticate(username=user, password=passwd)

            if usuario is not None:
                login(request, usuario)
                return redirect("inicio")
            
            else:
                messages.error(request, "Usuario no valido.")
        else:
            messages.error(request, "Información incorrecta.")

    form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('login')