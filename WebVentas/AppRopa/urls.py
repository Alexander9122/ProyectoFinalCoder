from django.http import request
from django.urls import path
from AppRopa import views




urlpatterns = [
    
    #URL para el inicio de la APP y para la clase Hombre, Mujer y Niños

    path('inicio', views.inicio, name="Inicio"),
    path('hombre', views.hombre, name="Hombre"),
    path('mujer', views.mujer, name="Mujer"),
    path('niños', views.niños, name="Niños"),

    #URL para la clase Hombre Formulario, Mujer Formulario y Niños Formulario

    path('hombreFormulario', views.hombreFormulario, name="HombreFormulario"),
    path('mujerFormulario', views.mujerFormulario, name="MujerFormulario"),
    path('niñosFormulario', views.niñosFormulario, name="NiñosFormulario"),

    #URL para la busqueda de Ropa para la clase Hombre, Mujer y Niños

    path('busquedaRopaHombre', views.busquedaRopaHombre, name="BusquedaRopaHombre"),
    path('busquedaRopaMujer', views.busquedaRopaMujer, name="BusquedaRopaMujer"),
    path('busquedaRopaNiños', views.busquedaRopaNiños, name="BusquedaRopaNiños"),

    #URL necesario para que muestre el resultado de la busqueda de Ropa para la clase Hombre, Mujer y Niños

    path('buscarRopaH/', views.buscarRopaH),
    path('buscarRopaM/', views.buscarRopaM),
    path('buscarRopaN/', views.buscarRopaN),

    #URL tambien necesario para mostrar el resultado de la busqueda de Ropa para la clase Hombre, Mujer y Niños

    path('resultadoBusquedaHombre', views.resultadoBusquedaHombre), 
    path('resultadoBusquedaMujer', views.resultadoBusquedaMujer), 
    path('resultadoBusquedaNiños', views.resultadoBusquedaNiños),

    #URL que muestra los datos que se crearon en base a cada clase (Hombre, Mujer y Niños)

    path('leerRopaHombre', views.leerRopaHombre, name="LeerRopaHombre"),
    path('leerRopaMujer', views.leerRopaMujer, name="LeerRopaMujer"),
    path('leerRopaNiños', views.leerRopaNiños, name="LeerRopaNiños"),

    #URL necesario para eliminar los datos creados en la clase Hombre, Mujer y Niños

    path('eliminarRopaHombre/<numero_para_borrar>/',views.eliminarRopaHombre,name="EliminarRopaHombre"),
    path('eliminarRopaMujer/<numero_para_borrar>/',views.eliminarRopaMujer,name="EliminarRopaMujer"),
    path('eliminarRopaNiños/<numero_para_borrar>/',views.eliminarRopaNiños,name="EliminarRopaNiños"),

    #URL necesario para editar los datos creados en la clase Hombre, Mujer y Niños

    path('editarRopaHombre/<numero_para_editar>/',views.editarRopaHombre,name="EditarRopaHombre"),
    path('editarRopaMujer/<numero_para_editar>/',views.editarRopaMujer,name="EditarRopaMujer"),
    path('editarRopaNiños/<numero_para_editar>/',views.editarRopaNiños,name="EditarRopaNiños"),

   
    
    

    

]