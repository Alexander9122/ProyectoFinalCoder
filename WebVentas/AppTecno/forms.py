from django import forms

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