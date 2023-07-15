from django import forms
from .models import Contacto, Noticia, Autor, Postulacion

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        #fields = ["nombre", "email", "telefono"] --> para mostrar ciertos capos
        fields = "__all__" #-> mostrar todos los campos del modelo Contacto


class RevisarForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ["categoria", "titulo", "subtitulo", "fecha", "cuerpo", "imagen"]
        widgets = {
            "fecha": forms.DateInput(attrs={'type':'date'},format=('%Y-%m-%d'))
        }



class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = "__all__"
        widgets = {
            "fecha": forms.DateInput(attrs={'type':'date'},format=('%Y-%m-%d'))
        }    

class AutoresForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = "__all__"


class PostulacionForm(forms.ModelForm):
    class Meta:
        model = Postulacion
        fields = "__all__"
        widgets = {
            "fecha_nacimiento": forms.DateInput(attrs={'type':'date'},format=('%Y-%m-%d'))
        }    