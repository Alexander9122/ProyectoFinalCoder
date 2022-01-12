from django.db.models import fields
from django.shortcuts import render
from django.http import HttpResponse
from AppHogar.models import *
from AppHogar.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.contrib.auth.decorators import login_required

@login_required
def hogar(request):
    return render(request, 'AppHogar/hogar.html')


def blanco(request):
    return render(request, 'AppHogar/blanco.html')


def cocinas(request):
    return render(request, 'AppHogar/cocinas.html')

def electrodomesticos(request):
    return render(request, 'AppHogar/electrodomesticos.html')

#AGREGAR BLANCO

def blancoForm(request):
    if request.method == "POST":
        miFormulario = BlancoFormulario(request.POST)

        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data

            blancoInsta = Blanco(marca=informacion["marca"], descripcion=informacion["descripcion"], color=informacion["color"], plazas=informacion["plazas"],precio=informacion["precio"])

            blancoInsta.save()

            return render(request, 'AppHogar/blanco.html')

    else:

        miFormulario = BlancoFormulario()


    return render (request, 'AppHogar/blancoForm.html ',{'miFormulario':miFormulario})


#Formulario para cargar cocinas 

def cocinasForm(request):
    if request.method == "POST":
        
        miFormulario = CocinaFormulario(request.POST)

        if  miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            cocina_insta = Cocinas(marca = informacion["marca"], color=informacion["color"], canti_hornallas=informacion["canti_hornallas"])
            cocina_insta.save()

            return render(request,'AppHogar/hogar.html')
    else:
            miFormulario = CocinaFormulario()
    return render(request,'AppHogar/cocinasForm.html', {'miFormulario':miFormulario})

#FORMULARIO ELECTRODOMESTICOS 

def electrodomesticosForm(request):
    if request.method == "POST":
        
        miFormulario = ElectrodomesticosFormulario(request.POST)

        if  miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            electro_insta = Electrodomesticos( tipo = informacion["tipo"],
                                               marca = informacion["marca"],
                                               descripcion  = informacion["descripcion"],
                                               modelo = informacion["modelo"],
                                               color=informacion["color"],  
                                               voltage=informacion["voltage"])
            electro_insta.save()

            return render(request,'AppHogar/hogar.html')
    else:
            miFormulario = ElectrodomesticosFormulario()
    return render(request,'AppHogar/electrodomesticosForm.html', {'miFormulario':miFormulario})



#FUNCION LEER
#BLANCOS
def leerBlancos(request):
    blancos = Blanco.objects.all()

    dir =  {'blancos': blancos} #contexto

    return render(request, 'AppHogar/leerBlancos.html', dir)
#COCINAS
def leerCocinas(request):
    cocinas = Cocinas.objects.all()

    dir =  {'cocinas': cocinas} #contexto

    return render(request, 'AppHogar/leerCocinas.html', dir)    
#ELECTRODOMESTICOS
def leerElectro(request):
    electrodomesticos = Electrodomesticos.objects.all()

    dir =  {'electrodomesticos': electrodomesticos} #contexto

    return render(request, 'AppHogar/leerElectrodomesticos.html', dir)   

#ELIMINAR BLANCO
def eliminarBlanco(request, nombreBorrar):

    blancoBorrar = Blanco.objects.get(descripcion=nombreBorrar)
    blancoBorrar.delete()

    blancos = Blanco.objects.all()

    dir =  {'blancos': blancos} #contexto

    return render(request, 'AppHogar/leerBlancos.html', dir)





#Editar blanco
def editarBlanco(request, descripcionEditar):

    blanco = Blanco.objects.get(descripcion=descripcionEditar)

    if request.method == "POST":

        miFormulario = BlancoFormulario(request.POST)

        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
             
            blanco.marca=informacion['marca']
            blanco.descripcion=informacion['descripcion']
            blanco.color=informacion['color']
            blanco.plazas=informacion['plazas']
            blanco.precio=informacion['precio']

            blanco.save()

            return render(request, 'AppHogar/leerBlanco.html')

    else:

        miFormulario = BlancoFormulario(initial={'marca':blanco.marca,'descripcion':blanco.descripcion,'color':blanco.color,'plazas':blanco.plazas,'precio':blanco.precio })
    
    return render (request, 'AppHogar/editarBlanco.html ',{'miFormulario':miFormulario, 'descripcionEditar':descripcionEditar })
