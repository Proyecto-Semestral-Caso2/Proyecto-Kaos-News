from django.contrib import admin
from .models import *

# Register your models here.




# Parametros para editar o mostra


class NoticiaAdmin(admin.ModelAdmin):
    list_display= ['categoria', 'titulo', 'subtitulo','autor', 'fecha', 'cuerpo', 'imagen']
    list_editable = ['categoria', 'titulo', 'subtitulo','autor', 'fecha', 'cuerpo', 'imagen']
    search_fields = ['nombre', 'autor', 'categoria']
    list_filter = ['autor']
  

# Habilitar acceso en pagina admin
# admin.site.register(Usuarios)
admin.site.register(Noticia)
admin.site.register(Contacto)

admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Postulacion)