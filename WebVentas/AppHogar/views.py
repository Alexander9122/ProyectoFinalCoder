from typing import List
from django.db.models import fields
from django.shortcuts import redirect, render
from django.http import HttpResponse
from AppHogar.models import *
from AppHogar.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
def blanco(request):
    return render(request, 'AppHogar/blanco.html')


def cocinas(request):
    return render(request, 'AppHogar/cocinas.html')


def electrodomesticos(request):
    return render(request, 'AppHogar/electrodomesticos.html')

    
# Formulario para cargar blancos
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
def cocinaForm(request):
    if request.method == "POST":
        miFormulario = CocinaFormulario(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            cocina_insta = Cocinas(marca = informacion["marca"], color=informacion["color"], canti_hornallas=informacion["canti_hornallas"])
            cocina_insta.save()

            return render(request,'AppHogar/cocinas.html')
    else:
            miFormulario = CocinaFormulario()
    return render(request,'AppHogar/cocinaForm.html', {'miFormulario':miFormulario})



#Formulario para cargar electrodomesticos
def electroForm(request):
    if request.method == "POST":
        miFormulario = ElectrodomesticosFormulario(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            electro_insta = Electrodomesticos(marca=informacion["marca"], descripcion=informacion["descripcion"],modelo=informacion["modelo"], color=informacion["color"], voltage=informacion["voltage"])
            electro_insta.save()

            return render(request,'AppHogar/electrodomesticos.html')
    else:
            miFormulario = ElectrodomesticosFormulario()
    return render(request,'AppHogar/electroForm.html', {'miFormulario':miFormulario})


def busquedaBlanco(request):
    return render(request, 'Apphogar/busquedaBlanco.html')


def buscar(request):

    if request.GET["descripcion"]:

        descripcion = request.GET["descripcion"]
        blanco =Blanco.objects.filter(descripcion__icontains=descripcion)
        return render(request,'AppHogar/resultadoBusqueda.html', {'blanco':blanco, 'descripcion':descripcion} )

       

    else:
        respuesta = 'ingresar informacion '   

    return HttpResponse(respuesta)



# Leer blancos
def leerBlanco(request):

    blancos = Blanco.objects.all()
    dir ={'blancos': blancos} # contexto
    return render(request, 'AppHogar/leerBlanco.html', dir)
 
 #Eliminar blancos
def eliminarBlanco(request, descripcionBorrar):

    blancoBorrar = Blanco.objects.get(descripcion=descripcionBorrar)
    blancoBorrar.delete()

    blanco = Blanco.objects.all()

    return render(request, 'AppHogar/leerBlanco.html', {"blanco":blanco})


#Editar blanco
def editarBlanco(request, descripcionEditar):
    blanco = Blanco.objects.get(descripcion=descripcionEditar)

    if request.method == "POST":

        miFormulario = BlancoFormulario(request.POST)

        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data

             
            blanco.marca=informacion["marca"]
            blanco.descripcion=informacion["descripcion"]
            blanco.color=informacion["color"]
            blanco.plazas=informacion["plazas"]
            blanco.precio=informacion["precio"]

            blanco.save()

            return render(request, 'AppHogar/leerBlanco.html')

    else:

        miFormulario = BlancoFormulario(initial={'marca':blanco.marca,'descripcion':blanco.descripcion,'color':blanco.color,'plazas':blanco.plazas,'precio':blanco.precio })
    
    return render (request, 'AppHogar/editarBlanco.html ',{'miFormulario':miFormulario, 'descripcionEditar':descripcionEditar })




#CBV ----> CRUD ----> cocinas

#LEER

class CocinaList(ListView):
    model = Cocinas
    template_name = "AppHogar/cocinas_list.html"

#DETALLE cocinas

class CocinaDetalle(DetailView):
    model = Cocinas
    template_name = "AppHogar/cocinas_detalle.html"


#CREAR cocinas

class CocinaCreacion(CreateView):
    model = Cocinas
    success_url ="../cocinas/list"
    fields = ['marca', 'color','canti_hornallas' ]

#MODIFICAR cocinas

class CocinasUpdate(UpdateView):
    model = Cocinas
    success_url ="../cocina/list"
    fields = ['marca', 'color','canti_hornallas' ]

#BORRAR cocinas

class CocinasDelete(DeleteView):
    model = Cocinas
    success_url ="../cocina/list"
    


