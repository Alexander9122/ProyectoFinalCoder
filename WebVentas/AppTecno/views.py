from django.shortcuts import render
from django.http import HttpResponse
from AppTecno.models import *
from AppTecno.forms import *

# Create your views here.
def inicio(request):

    return render (request, 'AppTecno/inicio.html')

def correcto(request):

    return render (request, 'AppTecno/correcto.html')


def laptops(request):

    if request.method == "POST":

        formularioLaptop = LaptopsFormulario(request.POST)

        if formularioLaptop.is_valid():

            informacion = formularioLaptop.cleaned_data
 
            laptopInsta = Laptops(  marca       = informacion["marca"], 
                                    pulgadas    = informacion["pulgadas"], 
                                    procesador  = informacion["procesador"], 
                                    ram         = informacion["ram"], 
                                    precio      = informacion["precio"])            

            laptopInsta.save() 

            return render (request, 'AppTecno/correcto.html')

    else:

        formularioLaptop = LaptopsFormulario()

    return render(request, 'AppTecno/laptops.html', {"formularioLaptop":formularioLaptop})


def celulares(request):

    if request.method == "POST":

        formularioCelular = CelularesFormulario(request.POST)

        if formularioCelular.is_valid():

            informacion = formularioCelular.cleaned_data
 
            celularInsta = Celulares(   marca           = informacion["marca"], 
                                        compania        = informacion["compania"], 
                                        conectividad    = informacion["conectividad"], 
                                        memoria         = informacion["memoria"], 
                                        precio          = informacion["precio"])            

            celularInsta.save() 

            return render (request, 'AppTecno/correcto.html')

    else:

        formularioCelular = CelularesFormulario()

    return render(request, 'AppTecno/celulares.html', {"formularioCelular":formularioCelular})


def televisores(request):

    if request.method == "POST":

        formularioTelevisores = TelevisoresFormulario(request.POST)

        if formularioTelevisores.is_valid():

            informacion = formularioTelevisores.cleaned_data
 
            televisorInsta = Televisores(   marca       = informacion["marca"], 
                                            pulgadas    = informacion["pulgadas"], 
                                            resolusion  = informacion["resolusion"], 
                                            precio      = informacion["precio"])            

            televisorInsta.save() 

            return render (request, 'AppTecno/correcto.html')

    else:

        formularioTelevisores = TelevisoresFormulario()

    return render(request, 'AppTecno/televisores.html', {"formularioTelevisores":formularioTelevisores})
    
def leerLaptops (request):

    laptops = Laptops.objects.all()

    contexto = {"laptops":laptops}

    return render (request, "AppTecno/leerLaptops.html", contexto)

def eliminaLaptop (request, numero_para_borrar):

    laptopBorrar = Laptops.objects.get(id=numero_para_borrar)
    laptopBorrar.delete()

    laptops = Laptops.objects.all() 

    contexto = {"laptops":laptops}

    return render(request, "AppTecno/leerLaptops.html", contexto)