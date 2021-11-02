"""donQuijote URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gestionCompra.models import Producto
from donQuijote import views
from django.conf import settings
from django.conf.urls.static import static

#from donQuijote.views import Hija2, saludo, Hija
#from gestionCompra import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="Inicio"),
    path('catalogo',views.catalogo, name="Catalogo"),
    path('contacto',views.contacto, name="Contacto"),
   # path('gestionCompra/', include('gestionCompra.urls')),
    path('categoria',views.categoria, name="Categoria"),
    #path('blog',views.blog, name="Blog"),
  
    #path('saludo/', saludo),
    #path('Hija/',Hija),
    #path('Hija2/', Hija2),
    #path('busquedaProducto/',views.busqueda_productos),
    #path('buscar/', views.buscar),
   # path('contacto/', views.contacto),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
