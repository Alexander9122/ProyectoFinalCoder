from django.shortcuts import render

#import recursos login
from AppInicio.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm,PasswordChangeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.

# Vistas Base Inicio----------------------------------------------------------------------------------------
def inicio(request):

    return render (request, 'AppInicio/inicio.html')

def about(request):

    return render (request, 'AppInicio/about.html')

#Login Inicio de Sesion -------------------------------------------------------------------------------------
def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username = usuario, password = contra)

            if user is not None:

                login(request, user)

                return render(request, "AppInicio/inicio.html", {"mensaje": f"Bienvenido {usuario}"})
            
            else:
                
                return render(request, "AppInicio/inicio.html", {"mensaje":"Error, datos incorrectos"})
        
        else:

            return render(request, "AppInicio/inicio.html", {"mensaje":"Error, fromulario erroneo"})
    
    form = AuthenticationForm()

    return render(request, "AppInicio/login.html", {'form':form})

# Creacion de Usuario ----------------------------------------------------------------------------------------
def register(request):

    if request.method == 'POST':

        form=UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request,"AppInicio/inicio.html", {"mensaje":"Usuario Creado"})
        
    else:

        form=UserRegisterForm()
        
    return render(request,"AppInicio/registro.html", {"form":form})


# Edicion de Datos de Usuario ----------------------------------------------------------------------------------
@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method=='POST':

        miFormulario = UserEditForm(request.POST)
        
        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.first_name      = informacion['first_name']
            usuario.last_name       = informacion['last_name']
            usuario.email           = informacion['email']
            usuario.password1       = informacion['password1']
            usuario.password2       = informacion['password2']
            usuario.save()

            return render(request, "AppInicio/inicio.html")
    
    else:

        miFormulario = UserEditForm(initial={'first_name': usuario.first_name,'last_name': usuario.last_name,'email':usuario.email})
    
    return render(request,"AppInicio/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})
