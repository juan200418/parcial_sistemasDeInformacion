from django.db import models

# Create your models here.
class Mensaje(models.Model):
    fondo = models.ImageField(upload_to='imagenes',null=True,blank=True ,default='/Deportes/media/encabesado.jpeg') 
    msj = models.CharField(max_length=200 , default="Landing Page Deportes")
    subtitulo = models.CharField(max_length=200 , default="¡Encuentra todo lo que necesita para mentenerte")
    def __str__(self):
        return self.msj+' - '+ self.subtitulo
    
class Producto(models.Model):
    imagen1 = models.ImageField(upload_to='imagenes',null=True,blank=True, default='/Deportes/media/estadio1.jpeg')
    imagen2 = models.ImageField(upload_to='imagenes',null=True,blank=True ,default='/Deportes/media/estadio2.jpeg')
    imagen3 = models.ImageField(upload_to='imagenes',null=True,blank=True ,default='/Deportes/media/estadio3.jpeg')
    imagen4 = models.ImageField(upload_to='imagenes',null=True,blank=True, default='/Deportes/media/estadio4.jpeg')
    nombre = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre 
    
class Deporte(models.Model):
    imagen= models.ImageField(upload_to='imagenes',null=True,blank=True ,default='/Deportes/media/deporte.jpeg')
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=300)
    def __str__(self):
        return self.nombre + '-' + self.descripcion
    
