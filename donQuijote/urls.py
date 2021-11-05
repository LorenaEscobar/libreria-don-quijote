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
from django.urls.conf import include
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
    path('categoria/<categoria_id>/',views.categoriaFiltrada, name="categoriaFiltrada"),
    path('carro/', include('carro.urls')),
    path('atencion',views.atencion, name="atencion"),
    path('envio',views.envio, name="envio"),
    path('pago',views.pago, name="pago"),
    path('local',views.local, name="local"),
  
    #path('saludo/', saludo),
    #path('Hija/',Hija),
    #path('Hija2/', Hija2),
    #path('busquedaProducto/',views.busqueda_productos),
    #path('buscar/', views.buscar),
   # path('contacto/', views.contacto),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
