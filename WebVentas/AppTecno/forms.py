from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):

    username        = forms.CharField()
    email           = forms.EmailField()
    password1       = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2       = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)

    last_name       = forms.CharField()
    first_name      = forms.CharField()
    imagen_avatar   = forms.ImageField(required=False)

    class Meta:
        model = User
        fields= ['username','email','password1','password2','last_name','first_name']
        help_text =  {k:"" for k in fields}



class LaptopsFormulario(forms.Form):
    
    marca = forms.CharField()
    pulgadas = forms.IntegerField()
    procesador = forms.CharField()
    ram = forms.CharField()
    precio = forms.FloatField()

class CelularesFormulario(forms.Form):

    marca = forms.CharField()
    compania = forms.CharField()
    conectividad = forms. CharField()
    memoria = forms.CharField ()
    precio = forms.FloatField ()

class TelevisoresFormulario(forms.Form):
    
    marca = forms.CharField()
    pulgadas = forms.IntegerField()
    resolusion = forms.CharField()
    precio = forms.FloatField()