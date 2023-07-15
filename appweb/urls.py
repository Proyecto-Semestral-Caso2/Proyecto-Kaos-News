from .views import *
from django.urls import path


urlpatterns = [
    path('home/', home, name="home"),
    path('', home, name="home"),
    path('categoria/<pk>', categoria, name="categoria"),
    path('categoria-chile/', categoria_chile, name="categoria-chile"),
    path('categoria-deportes/', categoria_deportes, name="categoria-deportes"),
    path('categoria-internacional/', categoria_internacional, name="categoria-internacional"),
    path('contacto/', contacto, name="contacto"),
    path('login_usuario/', login_usuario, name="login"),
    path('registro/', registro, name="registro"),
    path('mantenedor/crearNoticia/', crear_noticia, name="crear_noticia"),
    path('mantenedor/crearNoticiaAdmin/', crear_noticia_admin, name="crear_noticia_admin"),
    path('mantenedor/filtro_autor/', autores, name="filtro_autor"),
    path('mantenedor/listar_autor/', listar_autor, name="listar_autor"),
    path('mantenedor/modificar_autor/<pk>', modificar_autor, name="modificar_autor"),
    path('mantenedor/eliminar_autor/<pk>', eliminar_autor, name="eliminar_autor"),
    path('mantenedor/listarNoticia/', listar_noticia , name="listar_noticia"),
    path('mantenedor/eliminarNoticia', eliminar_noticia , name="eliminar_noticia"),
    path('mantenedor/modificarNoticia/<pk>', modificar_noticia , name="modificar_noticia"),
    path('mantenedor/modificarNoticiaAdmin/<pk>', modificar_noticia_admin , name="modificar_noticia_admin"),
    path('mantenedor/listarNoticiaAdmin', listar_noticia_admin , name="listar_noticia_admin"),
    path('mantenedor/eliminarNoticia/<pk>', eliminar_noticia , name="eliminar_noticia"),
    path('mantenedor/eliminarNoticiaAdmin/<pk>', eliminar_noticia_admin , name="eliminar_noticia_admin"),
    path('mantenedor/noticiaEliminarAdmin/<pk>', noticia_eliminar_admin , name="noticia_eliminar_admin"),
    path('contenido_noticia/<pk>/', contenidoNoticia, name="contenido_noticia"),
    path('categoria-chile/chile-1', chile1, name="chile-1"),
    path('categoria-chile/chile-2', chile2, name="chile-2"),
    path('categoria-deportes/deportes-1', deportes1, name="deportes-1"),
    path('categoria-deportes/deportes-2', deportes2, name="deportes-2"),
    path('categoria-internacional/internacional-1', internacional1, name="internacional-1"),
    path('categoria-internacional/internacional-2', internacional2, name="internacional-2"),
    path('postular', formulario_postulacion , name="formulario_postulacion"),
    path('mantenedor/postulaciones', listar_postulaciones , name="listar_postulaciones"),
    path('mantenedor/contenido_postulacion/<pk>/', detalle_postulacion , name="detalle_postulacion"),
    path('mantenedor/listar_solicitudes', listar_solicitudes , name="listar_solicitudes"),
    path('mantenedor/detalle_solicitudes/<pk>', detalle_solicitudes , name="detalle_solicitudes"),


    
]   