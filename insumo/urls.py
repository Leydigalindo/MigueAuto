from django.urls import path
from insumo.views import *


urlpatterns = [
    path('servicio/',servicio, name='servicio'),
    path ('insumo/', insumos, name='insumo'),
    path ('marca/', marca, name='marca'),
    
     #EDITAR Y ELIMINAR MARCA
    path ('marca/editarMarca/<int:id>', editarmarca, name='editarmarca'),
    path ('marca/editarMarca/<int:id>/<int:marca>', editarmarca, name='editarmarca'),
    path ('marca/eliminarMarca/<int:id>', eliminarMarca, name='eliminarMarca'),
    path ('insumo/eliminarInsumo/<int:id>', eliminarInsumo, name='eliminarInsumo'),
    path ('insumo/editarInsumo/<int:id>', editarInsumo, name='editarInsumo'),
    path ('servicio/eliminarServicio/<int:id>', eliminarServicio, name='eliminarServicio'),
    path ('servicio/editarServicio/<int:id>', editarServicio, name='editarServicio'),
    
    # TESTING
    path('testing/',testing, name='testing'),
]