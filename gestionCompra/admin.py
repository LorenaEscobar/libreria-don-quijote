from django.contrib import admin
from gestionCompra.models import Cliente, Producto, Categoria, Compra, Administrador

class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre", "apellido", "direccion", "telefono", "email")
    search_fields=("nombre", "apellido")


class ProductoAdmin(admin.ModelAdmin):
    list_filter=("nombre", ) #después poner por categoría
    list_display=("nombre", "autor", "editorial", "precio", "imagen")


class CompraAdmin(admin.ModelAdmin):
    list_display=("fecha", "total")
    list_filter=("fecha", )
    date_hierarchy="fecha"

class CategoriaAdmin(admin.ModelAdmin):
    list_display=("nombre", )
    list_filter=("nombre", )


# Register your models here.
admin.site.register(Cliente, ClientesAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Compra, CompraAdmin)
admin.site.register(Administrador)
