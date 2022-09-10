from importlib.resources import path


from .views import *
from django.urls import path


urlpatterns = [
    
    path ('generar/',generar_factura,name='generar_factura'),
    
    
    
    path('ver/<int:pk>',carrito, name="factura"),
    
    path('compras/', tiendas, name="clean_shop"),
    path('compras/<str:id>', tienda, name="Tienda"),
    
    # path('ver/<int:id>',add_cart, name="Tienda"),
    
    
    
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
    ]