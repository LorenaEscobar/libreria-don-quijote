from django.db import models

# Create your models de tablas here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    email = models.EmailField()
   

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=30)

    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'
        db_table='gestionCompra_categoria'

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    editorial = models.CharField(max_length=30)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='media')
    categoria=models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.RESTRICT)

    def __str__(self):
        return "El nombre es %s el autor es %s la editorial es %s y el precio es %s" %(self.nombre, self.autor, self.editorial, self.precio)



class Compra(models.Model):
    fecha = models.DateField()
    total = models.IntegerField()



class Administrador(models.Model):
    email = models.EmailField()
    contrasenia = models.CharField(max_length=8)

