from django.shortcuts import render

from django.http import HttpResponse

from AppRopa.models import Hombre, Mujer, Niños
from AppRopa.forms import HombreFormulario, MujerFormulario, NiñosFormulario

from django.contrib.auth.decorators import login_required

#Aca se crean las vistas de la pagina Web

#Primer vista
@login_required
def inicio(request):

    return render(request, 'AppRopa/ropa.html')


def hombre(request):

    return render(request, 'AppRopa/hombre.html')


def mujer(request):

    return render(request, 'AppRopa/mujer.html')


def niños(request):

    return render(request, 'AppRopa/niños.html')

#Formulario para cargar Ropa para Hombres

def hombreFormulario(request):

    if request.method == "POST":

        miFormulario = HombreFormulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            hombreInsta = Hombre(  #instancia de hombre

                talle = informacion["talle"],
                marca = informacion["marca"],
                color = informacion["color"],
                precio = informacion["precio"])

            hombreInsta.save() #Este save guarda los datos ingresados en la base de datos

            return render(request, 'AppRopa/ropa.html')

    else:

        miFormulario = HombreFormulario()

    return render(request, 'AppRopa/hombreFormulario.html', {"miFormulario":miFormulario})

#Formulario para cargar Ropa para Mujer

def mujerFormulario(request):

    if request.method == "POST":

        miFormulario = MujerFormulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            mujerInsta = Mujer(    #instancia de mujer
                
                talle = informacion["talle"],
                marca = informacion["marca"],
                color = informacion["color"],
                precio = informacion["precio"])

            mujerInsta.save() #Este save guarda los datos ingresados en la base de datos

            return render(request, 'AppRopa/ropa.html')

    else:

        miFormulario = MujerFormulario()

    return render(request, 'AppRopa/mujerFormulario.html', {"miFormulario":miFormulario})

#Formulario para cargar Ropa para Niños

def niñosFormulario(request):

    if request.method == "POST":

        miFormulario = NiñosFormulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            niñosInsta = Niños(       #instancia de niños
                
                talle = informacion["talle"],
                marca = informacion["marca"],
                color = informacion["color"],
                precio = informacion["precio"])

            niñosInsta.save() #Este save guarda los datos ingresados en la base de datos

            return render(request, 'AppRopa/ropa.html')

    else:

        miFormulario = NiñosFormulario()

    return render(request, 'AppRopa/niñosFormulario.html', {"miFormulario":miFormulario})

#def de busqueda para cada clase (Hombre, Mujer y Niños), necesario para las URL de busqueda

def busquedaRopaHombre(request): 

    return render(request, 'AppRopa/busquedaRopaHombre.html')

def busquedaRopaMujer(request):

    return render(request, 'AppRopa/busquedaRopaMujer.html')

def busquedaRopaNiños(request):

    return render(request, 'AppRopa/busquedaRopaNiños.html')

#def de buscar para cada clase (Hombre, Mujer y Niños), necesario para los html que muestran los resultados de la busqueda de ropa

def buscarRopaH(request):

    if request.GET["marca"]:

        marca = request.GET["marca"]

        hombre = Hombre.objects.filter(marca__icontains=marca)   

        return render(request, "AppRopa/resultadoBusquedaHombre.html", {"hombre":hombre, "marca":marca})

    else:

        respuesta = "Ingresar informacion"

    return HttpResponse(respuesta)

def buscarRopaM(request):

    if request.GET["marca"]:

        marca = request.GET["marca"]

        mujer = Mujer.objects.filter(marca__icontains=marca)   

        return render(request, "AppRopa/resultadoBusquedaMujer.html", {"mujer":mujer, "marca":marca})

    else:

        respuesta = "Ingresar informacion"

    return HttpResponse(respuesta)

def buscarRopaN(request):

    if request.GET["marca"]:

        marca = request.GET["marca"]

        niños = Niños.objects.filter(marca__icontains=marca)   

        return render(request, "AppRopa/resultadoBusquedaNiños.html", {"niños":niños, "marca":marca})

    else:

        respuesta = "Ingresar informacion"

    return HttpResponse(respuesta)

#def necesario para crear el template de resultados de busqueda para cada clase, esto luego se agrega en los def de buscar (Empieza a partir de la linea 133)

def resultadoBusquedaHombre(request):

    return render(request, "AppRopa/resultadoBusquedaHombre.html")

def resultadoBusquedaMujer(request):

    return render(request, "AppRopa/resultadoBusquedaMujer.html")

def resultadoBusquedaNiños(request):

    return render(request, "AppRopa/resultadoBusquedaNiños.html")

#def creado para los html de leer ropa para cada clase

def leerRopaHombre(request):

    ropahombre = Hombre.objects.all()

    dir = {"hombre":ropahombre} #dir = diccionario

    return render(request, "AppRopa/leerRopaHombre.html", dir)

def leerRopaMujer(request):

    ropamujer = Mujer.objects.all()

    dir = {"mujer":ropamujer} #dir = diccionario

    return render(request, "AppRopa/leerRopaMujer.html", dir)

def leerRopaNiños(request):

    ropaniños = Niños.objects.all()

    dir = {"niños":ropaniños} #dir = diccionario

    return render(request, "AppRopa/leerRopaNiños.html", dir)

#def necesario para eliminar los datos creados, los mismos se eliminan desde los html leer ropa

def eliminarRopaHombre(request, numero_para_borrar):

    ropaHombreBorrar = Hombre.objects.get(id = numero_para_borrar)

    ropaHombreBorrar.delete()

    hombre = Hombre.objects.all()

    contexto = {"hombre":hombre}

    return render(request, "AppRopa/leerRopaHombre.html", contexto)

def eliminarRopaMujer(request, numero_para_borrar):

    ropaMujerBorrar = Mujer.objects.get(id = numero_para_borrar)

    ropaMujerBorrar.delete()

    mujer = Mujer.objects.all()

    contexto = {"mujer":mujer}

    return render(request, "AppRopa/leerRopaMujer.html", contexto)

def eliminarRopaNiños(request, numero_para_borrar):

    ropaNiñosBorrar = Niños.objects.get(id = numero_para_borrar)

    ropaNiñosBorrar.delete()

    niños = Niños.objects.all()

    contexto = {"niños":niños}

    return render(request, "AppRopa/leerRopaNiños.html", contexto)

##def necesario para editar los datos creados, los mismos se eliminan desde los html leer ropa

def editarRopaHombre(request, numero_para_editar):

    ropaH = Hombre.objects.get(id = numero_para_editar)

    if request.method == "POST":

        miFormulario = HombreFormulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            ropaH.talle = informacion["talle"]
            ropaH.marca = informacion["marca"]
            ropaH.color = informacion["color"]
            ropaH.precio = informacion["precio"]

            ropaH.save() #guarda los datos en la base de datos

            return render(request, 'AppRopa/ropa.html')

    else:

        miFormulario = HombreFormulario(initial={"talle":ropaH.talle, "marca":ropaH.marca, "color":ropaH.color, "precio":ropaH.precio})

    return render(request, 'AppRopa/editarRopaHombre.html', {"miFormulario":miFormulario, "numero_para_editar":numero_para_editar})

def editarRopaMujer(request, numero_para_editar):

    ropaM = Mujer.objects.get(id = numero_para_editar)

    if request.method == "POST":

        miFormulario = MujerFormulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            ropaM.talle = informacion["talle"]
            ropaM.marca = informacion["marca"]
            ropaM.color = informacion["color"]
            ropaM.precio = informacion["precio"]

            ropaM.save() #guarda los datos en la base de datos

            return render(request, 'AppRopa/ropa.html')

    else:

        miFormulario = MujerFormulario(initial={"talle":ropaM.talle, "marca":ropaM.marca, "color":ropaM.color, "precio":ropaM.precio})

    return render(request, 'AppRopa/editarRopaMujer.html', {"miFormulario":miFormulario, "numero_para_editar":numero_para_editar})

def editarRopaNiños(request, numero_para_editar):

    ropaN = Niños.objects.get(id = numero_para_editar)

    if request.method == "POST":

        miFormulario = NiñosFormulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            ropaN.talle = informacion["talle"]
            ropaN.marca = informacion["marca"]
            ropaN.color = informacion["color"]
            ropaN.precio = informacion["precio"]

            ropaN.save() #guarda los datos en la base de datos

            return render(request, 'AppRopa/ropa.html')

    else:

        miFormulario = NiñosFormulario(initial={"talle":ropaN.talle, "marca":ropaN.marca, "color":ropaN.color, "precio":ropaN.precio})

    return render(request, 'AppRopa/editarRopaNiños.html', {"miFormulario":miFormulario, "numero_para_editar":numero_para_editar})










