from django import forms

#Formulario para cargar blanco  
class BlancoFormulario(forms.Form):
    marca = forms.CharField(max_length=60)
    descripcion = forms.CharField(max_length=60)
    color = forms.CharField(max_length=30)
    plazas = forms.IntegerField()
    precio = forms.IntegerField()

#Formulario para cargar cocinas
class CocinaFormulario(forms.Form):
    marca = forms.CharField(max_length=60)
    color = forms.CharField(max_length=30)    
    canti_hornallas = forms.IntegerField()
    
#Formulario para cargar electrodomesticos    
class ElectrodomesticosFormulario(forms.Form):
    tipo = forms.CharField(max_length=60) 
    marca = forms.CharField(max_length=60)
    descripcion = forms.CharField(max_length=60)
    modelo = forms.CharField(max_length=60)
    color = forms.CharField(max_length=30) 
    voltage = forms.IntegerField()    