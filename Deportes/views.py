from django.http import HttpResponse
from.import models
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Producto

# Create your views here.
def tiendaDeportes(request):
    mensaje = models.Mensaje.objects.first()
    Producto= models.Deporte.objects.all()
    datos ={
        'titulo':mensaje.msj,
        'subtitulo':mensaje.subtitulo,
        'Deporte':Producto
    }
    return render(request, 'index.html',datos)

def galeriaFotos(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'galeriaFotos.html', {'producto': producto})

def galeriaFotos2(request):
    mensaje = models.Mensaje.objects.first()
    Producto= models.Producto.objects.all()
    datos ={
        'titulo':mensaje.msj,
        'subtitulo':mensaje.subtitulo,
        'Producto':Producto
    }
    print (Producto)
    return render(request, 'galeriaFotos.html',datos)