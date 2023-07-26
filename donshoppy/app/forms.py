from django import forms
from .models import Contacto,Zapatilla,Mochila,Ropa,Producto,Servicio,Herramienta,Abarrote,Outdoor
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
class ContactoForm(forms.ModelForm):
    class Meta:
        model=Contacto
        fields =["nombre","correo","comentario"]

class ProductoForm(forms.ModelForm):
    class Meta:
        model=Producto
        fields = '__all__'

class ZapatillaForm(forms.ModelForm):
    class Meta:
        model=Zapatilla
        fields = '__all__'

class MochilaForm(forms.ModelForm):
    class Meta:
        model=Mochila
        fields = '__all__'


class RopaForm(forms.ModelForm):
    class Meta:
        model=Ropa
        fields = '__all__'
    
class ServicioForm(forms.ModelForm):
    class Meta:
        model=Servicio
        fields = '__all__'

class HerramientaForm(forms.ModelForm):
    class Meta:
        model=Herramienta
        fields = '__all__'

class AbarroteForm(forms.ModelForm):
    class Meta:
        model=Abarrote
        fields = '__all__'
    
class OutdoorForm(forms.ModelForm):
    class Meta:
        model=Outdoor
        fields = '__all__'




class CustomUserCreationForm(UserCreationForm):
    direccion = forms.CharField(max_length=100)
    telefono = forms.CharField(max_length=20)
    class Meta:
        model= User
        fields = ['username', "first_name", "last_name","email","password1","password2"]