from django.contrib import admin
from .models import Mensaje,Producto,Deporte,Estadio
# Register your models here.
admin.site.register(Mensaje)
admin.site.register(Producto)
admin.site.register(Deporte)
admin.site.register(Estadio)
