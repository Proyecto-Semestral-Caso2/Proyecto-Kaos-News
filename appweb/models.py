from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
import datetime


# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=150, null=True)
    imagen = models.ImageField(upload_to="imagenes_perfil", null=True)
    descripcion = RichTextField(null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        
       texto="{0}"
       return texto.format(self.nombre)

class Categoria(models.Model):
    nombre=models.CharField(max_length=150)
    def __str__(self):
        return self.nombre


estados_noticia = [
    [0, "Creada"],
    [1, "Aprobada"],
    [2, "Rechazada"],
]

class Noticia(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    titulo = models.CharField(max_length=150)
    subtitulo = models.CharField(max_length=250)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, null=True)
    fecha = models.DateField()
    cuerpo = RichTextField(null=True)    
    imagen = models.ImageField(upload_to="imagenes_noticias", null=True)
    motivo = models.TextField(null=True)
    estado = models.IntegerField(choices=estados_noticia, default=0)
        
    def __str__(self):
        texto="{0} / {1} / {2}"
        return  texto.format(self.categoria, self.titulo, self.autor)
    

tipos_contacto = [
    [0, "Sugerencia"],
    [1, "Reclamo"],
    [2, "Felicitaciones"],
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    telefono = models.IntegerField()
    tipo_contacto = models.IntegerField(choices=tipos_contacto, null=True)
    mensaje = RichTextField(null=True)
    def __str__(self):
        texto="{0} / {1}"
        return texto.format(self.email, self.nombre)



class Postulacion(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField(null=True)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to="imagenes_postulantes", null=True)
    descripcion = RichTextField(null=True) 

        
    def __str__(self):
        texto="{0} / {1}"
        return  texto.format(self.nombre, self.apellido)

