from django import forms

# Formulario de la clase Hombre

class HombreFormulario(forms.Form):

    talle = forms.CharField(max_length=40)
    marca = forms.CharField(max_length=40)
    color = forms.CharField(max_length=40)
    precio = forms.IntegerField()

# Formulario de la clase Mujer

class MujerFormulario(forms.Form):

    talle = forms.CharField(max_length=40)
    marca = forms.CharField(max_length=40)
    color = forms.CharField(max_length=40)
    precio = forms.IntegerField()

# Formulario de la clase Niños

class NiñosFormulario(forms.Form):

    talle = forms.CharField(max_length=40)
    marca = forms.CharField(max_length=40)
    color = forms.CharField(max_length=40)
    precio = forms.IntegerField()