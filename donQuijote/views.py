from django.http import HttpResponse
import datetime
from django.core.mail import send_mail
from django.template import loader
from django.conf import settings
from django.shortcuts import render

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



 