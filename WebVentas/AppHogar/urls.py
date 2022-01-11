from django.urls import path
from AppHogar import views


urlpatterns = [
    path('blanco', views.blanco, name='Blanco' ),
    path('cocinas',views.cocinas, name='Cocinas'),
    path('electrodomesticos', views.electrodomesticos, name='Electrodomesticos'),
    path('blancoForm', views.blancoForm, name='BlancoForm' ),
    path('cocinaForm', views.cocinaForm, name='CocinasForm' ),
    path('electroForm', views.electroForm, name='ElectroForm' ),
    path('busquedaBlanco', views.busquedaBlanco ),
    path('buscar/', views.buscar),
    path('leerBlanco/', views.leerBlanco, name= 'LeerBlanco'),
    path('eliminarBlanco/<descripcionBorrar>', views.eliminarBlanco, name= 'EliminarBlanco'),
    path('editarBlanco/<descripcionEditar>', views.editarBlanco, name= 'EditarBlanco'),
   
   
   #CLASES BASADAS EN VISTAS DJANGO
    path('cocinas_list', views.CocinaList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.CocinaDetalle.as_view(), name='Detail'),
    path(r'^nuevo$',views.CocinaCreacion.as_view(),name='New'),
    path(r'^editar/(?P<pk>\d+)$',views.CocinasUpdate.as_view(),name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$',views.CocinasDelete.as_view(),name='Delete'),
    
    
    
    

    

]
