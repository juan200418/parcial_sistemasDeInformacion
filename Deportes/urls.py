from django.urls import path
from . import views 

urlpatterns = [
    path("", views.tiendaDeportes, name='tienda_deportes'),  # Ruta para la vista tiendaDeportes
    path('producto/', views.galeriaFotos2, name='galeriaFotos'),
    path('detalle_estadios/', views.DetalleEstadios, name='DetalleEstadios'),
]
