from django import forms

#import Login
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

#Creacion de Ususario
class UserRegisterForm(UserCreationForm):
    
    first_name      = forms.CharField(label='Nombre')
    last_name       = forms.CharField(label='Apellido')
    username        = forms.CharField()
    email           = forms.EmailField()
    password1       = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2       = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)

   
#    imagen_avatar   = forms.ImageField(required=False)

    class Meta:
        model = User
        fields= ['first_name', 'last_name', 'email', 'username','password1','password2']
        help_text =  {k:"" for k in fields}

#Modificacion de Ususario
class UserEditForm(UserCreationForm):


    first_name      = forms.CharField()
    last_name       = forms.CharField()
    email           = forms.EmailField(label='Modificar E-mail')
    password1       = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2       = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)

    class Meta:
       model = User
       fields= [ 'first_name','last_name','email','password1','password2']
       help_text =  {k:"" for k in fields}
