from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *
from .forms import * 
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

# home
def home(request):


    
    return render(request, "home.html")
    

# crear
@login_required(login_url="/accounts/login")
@permission_required(['appweb.add_noticia'], login_url="/accounts/login")
def crear_noticia(request):
    autor = Autor.objects.get(usuario=request.user)
    data={
        'form_revisar':RevisarForm,
        "mensaje": "",
    }

    if request.method=="POST":
        formulario = RevisarForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            creacion = formulario.save(commit=False)
            creacion.autor = autor
            creacion.save()
            data["mensaje"] = "Noticia Creada"
            return redirect(to="listar_noticia")
        else:
            data["mensaje"] = "Error"
            data["form_revisar"] = formulario

    return render(request, "mantenedor/crearNoticia.html", data)

@login_required(login_url="/accounts/login")
@permission_required(['appweb.delete_noticia'], login_url="/accounts/login")
def crear_noticia_admin(request):
    data={
        'form_noticia':NoticiaForm,
        "mensaje": "",
    }

    if request.method=="POST":
        formulario = NoticiaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            creacion = formulario.save(commit=False)            
            creacion.save()
            data["mensaje"] = "Noticia Creada"
            return redirect(to="noticia_publicada_admin")
        else:
            data["mensaje"] = "Error"
            data["form_noticia"] = formulario

    return render(request, "mantenedor/crearNoticia_admin.html", data)


@login_required(login_url="/accounts/login")
@permission_required(['appweb.delete_autor'], login_url="/accounts/login")
def listar_autor(request):
    
    listarAutores = Autor.objects.all()

    data={
        'listarAdmin' : listarAutores
    }

    return render(request, "mantenedor/listar_autor.html", data)


@login_required(login_url="/accounts/login")
@permission_required(['appweb.delete_autor'], login_url="/accounts/login")
def modificar_autor(request, pk):
    modificar = get_object_or_404(Autor, pk=pk)
    data={
        'form_autormodi': AutoresForm(instance=modificar)
    }

    if request.method == 'POST':
        formulario = AutoresForm(data=request.POST, instance=modificar, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_autor")
        else : 
            data["mensaje"] = "hubo un error"
            data["form_autormodi"] = formulario

    return render(request, "mantenedor/modificar_autor.html", data)

@login_required(login_url="/accounts/login")
@permission_required(['appweb.delete_autor'], login_url="/accounts/login")
def eliminar_autor(request, pk):

    autor = Autor.objects.get(usuario=User.id)
    eliminar = get_object_or_404(User, pk = pk)
    if autor.delete():
        eliminar.delete()
    
    
    return redirect(to="listar_autor")

#listares

@login_required(login_url="/accounts/login")
@permission_required(['appweb.add_noticia'], login_url="/accounts/login")
def listar_noticia(request):
    autor = Autor.objects.get(usuario=request.user)
    listar = Noticia.objects.filter(autor=autor)

    data={
        'listar' : listar

    }

    return render(request, "mantenedor/listarNoticia.html", data)




def autores(request):
    periodistas = Autor.objects.all()
    data = {
        'mis_periodistas': periodistas
    }
    return render(request, "filtro_autor.html", data)




@login_required(login_url="/accounts/login")
@permission_required(['appweb.delete_noticia'], login_url="/accounts/login")
def listar_noticia_admin(request):
    
    listarAdmin = Noticia.objects.all()
    data={
        'listarAdmin' : listarAdmin
    }

    return render(request, "mantenedor/listarNoticia_admin.html", data)




#modificares
@login_required(login_url="/accounts/login")
@permission_required(['appweb.add_noticia'], login_url="/accounts/login")
def modificar_noticia(request, pk):
    modificar = get_object_or_404(Noticia, pk=pk)
    data={
        'form_modificar': RevisarForm(instance=modificar)
    }

    if request.method == 'POST':
        formulario = RevisarForm(data=request.POST, instance=modificar, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_noticia")
        else : 
            data["mensaje"] = "hubo un error"
            data["form_modificar"] = formulario


    return render(request, "mantenedor/modificar_noticia.html", data)

@login_required(login_url="/accounts/login")
@permission_required(['appweb.delete_noticia'], login_url="/accounts/login")
def modificar_noticia_admin(request, pk):
    modificar = get_object_or_404(Noticia, pk=pk)
    data={
        'form_modiadmin': NoticiaForm(instance=modificar)
    }

    if request.method == 'POST':
        formulario = NoticiaForm(data=request.POST, instance=modificar, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_noticia_admin")
        else : 
            data["mensaje"] = "hubo un error"
            data["form_modiadmin"] = formulario

    return render(request, "mantenedor/modificar_noticia_admin.html", data)




@login_required(login_url="/accounts/login")
@permission_required(['appweb.add_noticia'], login_url="/accounts/login")
def eliminar_noticia(request, pk):
    eliminar = get_object_or_404(Noticia, pk = pk)
    eliminar.delete()
    return redirect(to="listar_noticia")

@login_required(login_url="/accounts/login")
@permission_required(['appweb.delete_noticia'], login_url="/accounts/login")
def eliminar_noticia_admin(request, pk):
    eliminar = get_object_or_404(Noticia, pk = pk)
    eliminar.delete()
    return redirect(to="listar_noticia_admin")

@login_required(login_url="/accounts/login")
@permission_required(['appweb.delete_noticia'], login_url="/accounts/login")
def noticia_eliminar_admin(request, pk):
    eliminar = get_object_or_404(Noticia, pk = pk)
    eliminar.delete()
    return redirect(to="noticia_publicada_admin")





# categorias

# chile
def categoria_chile(request):      
    categoriaChile = Noticia.objects.filter(categoria = 1, estado = 1)
  
    data={
        'categoriaChile':categoriaChile,
        
    } 
    return render(request, "categoria-chile.html", data)

def cat_chile_buscar(request):
    buscar = Noticia.objects.all()

    valor_buscado = request.POST.get("valor_buscado")
    print(valor_buscado)
    data={
        'buscar': buscar 
    }
    return render(request, "categoria-chile.html", data)


#internacional
def categoria_internacional(request):
    catinter = Noticia.objects.filter(categoria = 2, estado = 1)
  

    return render(request, "categoria-internacional.html", {"cat_inter": catinter})


# deportes
def categoria_deportes(request):
    catdeportes = Noticia.objects.filter(categoria = 3, estado = 1)
   

    return render(request, "categoria-deportes.html", {"cat_deportes": catdeportes})


# formularios
def contacto(request):

    data = {
        'form': ContactoForm,
        'mensaje':"",
    }
    if request.method == "POST":
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Su mensaje ha sido enviado"
        else:
            data['form'] = formulario
            data['mensaje'] = "Ocurrio un error"

    return render(request, "contacto.html", data)



def formulario_postulacion(request):

    data={
        "form_postulacion": PostulacionForm,
        "mensaje": ""
    }

    if request.method == "POST":
        formulario = PostulacionForm(data=request.POST, files=request.FILES)

        if formulario.is_valid():

            formulario.save()
            data["mensaje"] = "Postulación Enviada"

        else:
            data["mensaje"] = "Error"
            data["form_postulacion"] = formulario

    return render(request, "postulacion.html", data)


@login_required(login_url="/accounts/login")
@permission_required(['appweb.view_postulacion'], login_url="/accounts/login")
def detalle_postulacion(request, pk):

    postulacion = get_object_or_404(Postulacion, pk=pk)
    det_postulacion = Postulacion.objects.filter(pk=pk)

    data = { 

        "post": postulacion,
        "detalle_post":  det_postulacion
    }

    return render(request,"mantenedor/detalle_postulacion.html", data)


@login_required(login_url="/accounts/login")
@permission_required(['appweb.view_postulacion'], login_url="/accounts/login")
def listar_postulaciones(request):

    
    listarPostulaciones = Postulacion.objects.all()

    data={
        "listarPostulacion" : listarPostulaciones
    }

    return render(request, "mantenedor/listar_postulacion.html", data)


@login_required(login_url="/accounts/login")
@permission_required(['appweb.delete_noticia'], login_url="/accounts/login")

def listar_solicitudes(request):
    listarSolicitudes = Contacto.objects.all()

    data={
        "listarSolicitud": listarSolicitudes
    }
    return render(request, "mantenedor/listar_solicitudes.html", data)


@login_required(login_url="/accounts/login")
@permission_required(['appweb.delete_noticia'], login_url="/accounts/login")
def detalle_solicitudes(request, pk):

    solicitud = get_object_or_404(Contacto, pk=pk)
    det_solicitud = Contacto.objects.filter(pk=pk)

    data = { 

        "post": solicitud,
        "detalle_post":  det_solicitud
    }

    return render(request,"mantenedor/detalle_solicitud.html", data)



#login y registro

def login_usuario(request):
   
    print("Bienvenido: "+ request.user.username)
    print("Ha iniciado sesión a CaosNews")

    return redirect(to='home')

@login_required(login_url="/accounts/login")
@permission_required(['appweb.delete_noticia'], login_url="/accounts/login")
def registro(request):

    data = {
        "mensaje": ""
    }
    if request.POST:
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        correo = request.POST.get("correo")
        imagen = request.FILES["imagen"]
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 != password2:
            data["mensaje"] = "Las contraseñas deben ser identicas"
        else: 
            usu = User()
            usu.set_password(password1)
            usu.email=correo
            usu.username=nombre
            usu.last_name=apellido
            usu.first_name=nombre
            grupo = Group.objects.get(name='Usuario')
        try:
            usu.save()
            aut = Autor()
            aut.nombre = nombre + ' ' + apellido
            aut.usuario = usu
            aut.imagen = imagen
            aut.save()
            usu.groups.add(grupo)
            data["mensaje"]='Usuario creado correctamente'
            return redirect(to="listar_autor")
            

        except:
            data["mensaje"]='Error al registrar usuario'


    return render(request, "registration/registro.html", data)




def contenidoNoticia(request, pk):

    noticia = get_object_or_404(Noticia, pk=pk)
    cont_noticia = Noticia.objects.filter(pk=pk)
    

    data = { 

        "noti": noticia,
        "contenido_noti":  cont_noticia,
        
    }

    

    return render(request, "contenido_noticia.html", data)

def categoria(request, pk):

    cat = get_object_or_404(Categoria, pk=pk)
    

    data = { 

        "cat": cat,
        
    }

    return render(request, "categoria.html", data)


def chile1(request):
    return render(request, "chile-1.html")
def chile2(request):
    return render(request, "chile-2.html")
def deportes1(request):
    return render(request, "deportes-1.html")
def deportes2(request):
    return render(request, "deportes-2.html")

def internacional1(request):
    return render(request, "internacional-1.html")
def internacional2(request):
    return render(request, "internacional-2.html")





