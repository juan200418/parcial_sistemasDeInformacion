from django.shortcuts import render, get_object_or_404
from .models import Mensaje, Producto, Deporte, Estadio

def tiendaDeportes(request):
    mensaje = Mensaje.objects.first()
    deportes = Deporte.objects.all()
    datos ={
        'titulo': mensaje.msj if mensaje else "Landing Page Deportes",
        'subtitulo': mensaje.subtitulo if mensaje else "¡Encuentra todo lo que necesita para mentenerte",
        'Deporte': deportes
    }
    return render(request, 'index.html', datos)

def galeriaFotos(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'galeriaFotos.html', {'producto': producto})

def galeriaFotos2(request):
    mensaje = Mensaje.objects.first()
    productos = Producto.objects.all()
    datos ={
        'titulo': mensaje.msj if mensaje else "Landing Page Deportes",
        'subtitulo': mensaje.subtitulo if mensaje else "¡Encuentra todo lo que necesita para mentenerte",
        'Producto': productos
    }
    return render(request, 'galeriaFotos.html', datos)

def DetalleEstadios(request):
    mensaje = Mensaje.objects.first()
    estadios = Estadio.objects.all()
    datos_estadios = []

    for estadio in estadios:
        datos_estadios.append({
            'nombre': estadio.nombre,
            'pais': estadio.pais,
            'descripcion': estadio.descripcion,
            'imagen1_url': estadio.imagen1.url,
            'imagen2_url': estadio.imagen2.url,
            'imagen3_url': estadio.imagen3.url,
            'imagen4_url': estadio.imagen4.url,
        })

    datos = {
        'titulo': mensaje.msj if mensaje else "Landing Page Deportes",
        'subtitulo': mensaje.subtitulo if mensaje else "¡Encuentra todo lo que necesita para mentenerte",
        'estadios': datos_estadios,
    }
    return render(request, 'detalle_estadios.html', datos)
