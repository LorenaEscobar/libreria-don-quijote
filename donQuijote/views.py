
import datetime
from django.core.mail import send_mail
from django.http import request
from django.template import loader
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from gestionCompra.models import Categoria, Producto

def home(request):
    return render(request, "inicio.html")


def catalogo(request):
    productos= Producto.objects.all()
    return render(request, "catalogo.html", {"productos":productos})

def contacto(request):
    return render(request, "contacto.html", {})


#def blog(request):
#    return render(request,"blog.html")


def categoriaFiltrada(request, categoria_id):
    cat=Categoria.objects.get(id=categoria_id)
    productos=Producto.objects.filter(categoria=cat)
    return render(request, "categoriaFiltrada.html", {"categoria":cat, "productos":productos})
    

def categoria(request):
    categorias= Categoria.objects.all()
    return render(request, "categoria.html", {"categorias":categorias})







def contacto(request):

    if request.method=="POST":
        subject=request.POST["asunto"]
        message=request.POST["mensaje"]+" "+request.POST["email"]
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["blue_gaia@hotmail.com"]
        send_mail(subject, message,email_from,recipient_list)
      
    
    return render(request, "contacto.html")





class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

def saludo(request):
    p1=Persona("Lorena", "Escobar")
    ahora=datetime.datetime.now()
  
    return render(request, "estilo1.html", {"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual": ahora})

def Hija(request):
        fecha_actual = datetime.datetime.now()
        return render(request, "hija1.html", {"dameFecha":fecha_actual})

def Hija2(request):
        fecha_actual = datetime.datetime.now()
        return render(request, "hija2.html", {"dameFecha":fecha_actual})

def atencion(request):
    return render(request, "atencion.html", {})


def envio(request):
    return render(request, "envio.html", {})


def pago(request):
    return render(request, "pago.html", {})

def local(request):
    return render(request, "local.html", {})

def carrito(request):
    return render(request, "carro/carrito.html", {})

def registro(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("http://127.0.0.1:8000/")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
    form = UserCreationForm
    return render(request, "registro.html", {"form":form})



 