from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class Curso_formulario(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    camada = forms.IntegerField()
    
class Profesor_formulario(forms.Form):
    
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length = 20) 
    curso = forms.CharField(max_length = 40) 
    email = forms.CharField(max_length=50)
    contraseña = forms.CharField(max_length=30)
    
class Alumno_formulario(forms.Form):
    
    nombre = forms.CharField(max_length = 20)
    apellido = forms.CharField(max_length = 20) 
    email = forms.EmailField(max_length = 50)
    contraseña = forms.CharField(max_length = 30)
    
class UserEditForm(UserCreationForm):
    
    email = forms.EmailField(label = "E-mail")
    password1 = forms.CharField(label = "Contraseña" , widget = forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir la contraseña" , widget = forms.PasswordInput)
    
    class Meta:
        
        model = User
        fields = ['email' , 'password1' , 'password2']
        help_text = {k : "" for k in fields}

class ProfesorEditForm(UserCreationForm):
    email = forms.EmailField(label = "E-mail")
    password1 = forms.CharField(label = "Contraseña" , widget = forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir la contraseña" , widget = forms.PasswordInput)
        
    class Meta:
        
        model = User
        fields = ['email' , 'password1' , 'password2']
        help_text = {k : "" for k in fields}