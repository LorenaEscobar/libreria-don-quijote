from django.http.response import HttpResponse
from django.shortcuts import render
from gestionCompra.models import Producto
from django.core.mail import send_mail
from django.conf import settings
from gestionCompra.forms import FormularioContacto

# Create your views here.
def busqueda_productos(request):
    return render(request, "busquedaProducto.html")

def buscar(request):
    if request.GET["prd"]:
        libros=request.GET["prd"]
        if len(libros)>60:
            mensaje="Texto de búsqueda muy largo"
        else:
            
            productos=Producto.objects.filter(nombre__icontains=libros)
            return render(request, "resultado_busqueda.html", {"productos":productos, "query":libros})
    else:
        mensaje="No has introducido nada"

    return HttpResponse(mensaje)

def contactoo(request):

    if request.method=="POST":
        subject=request.POST["asunto"]
        message=request.POST["mensaje"]+" "+request.POST["email"]
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["blue_gaia@hotmail.com"]
        send_mail(subject, message,email_from,recipient_list)
      
    
    return render(request, "contacto.html")

     # miFormulario=FormularioContacto(request.POST)

    #  if miFormulario.is_valid():
    #      infForm= miFormulario.cleaned_data

    #      send_mail(infForm['asunto'], infForm['mensaje'], 
     #     infForm.get('email',''),['blue_gaia@hotmail.com'],)

      #    return(request,"resultadoBusqueda.html")

    #else:
    #    miFormulario=FormularioContacto()

    #return render(request, "formulario_contacto.html", {"form":miFormulario})"""