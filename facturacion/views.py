from django.shortcuts import render, redirect
from facturacion.forms import *
from registro.models import *
from datetime import datetime
from django.db.models import Sum
from django.contrib import messages
from facturacion.compras import Carrito
from insumo.models import *
from registro.views import usuario, vehiculo

# Create your views here.


def generar_factura(request):
    factura_db = Generar.objects.all() # se carga la base de datos para generar la factura
    usuarios = Usuario.objects.all() # se carga la base de datos para cargar los usuarios en los selects
    vehiculos = Vehículo.objects.all() # se carga la base de datos para cargar los vehiculos en los selets
    Hora = datetime.now() #hora en la que se genera la factura
    if request.method == 'POST': # si el metodo request es post
        factura = FacturaForm(request.POST) # muesta la factura con sus datos
        print(request.POST)
        if factura.is_valid():# so la factura es valida
            usuario = Usuario.objects.get(id=request.POST['usuario']) #se le asigna el dato cargado a la variable
            vehiculo = Vehículo.objects.get(id=request.POST['vehiculo']) #se le asigna el dato cargado a la variable
            aux = Generar.objects.create(
                fecha=Hora.strftime("%d/%m/%y %H:%M:%S"),
                usuario=usuario,
                vehiculo=vehiculo,
            )#se crea la factura
            messages.success(request, f'Factura agregada    corretamente.')#Mensaje de exito
            print('se ah logrado hacer la factura ')
            
            return redirect('Tienda',aux.id)#Me redirija a la tienda con el id de la factura
        else:# si no
            print("formulario invalido") # Se imprime en la consola que tenemos errores
    else:# a menos que no sea post
        factura = FacturaForm()# se  seguira cargando el factura form
    
    context = { #se pasan las variables por el contexto a las plantillas
        'form': factura,
        'factura_db': factura_db,
        'usuario': usuarios,
        'vehiculo': vehiculos,
    }
    return render(request, 'facturacion/generar.html', context)

def agregar_servicios(request):
    pass




def tienda(request,id):
    productos = Insumo.objects.all()
    datos_factura = Generar.objects.get(id=id)
    if request.method == 'POST' and 'factura' in request.POST:
            aux = Compras.objects.create(id=id,factura=datos_factura,estado='Activo',tipodeservicio='Latoneria',)
            return redirect("factura", aux.id)
    context ={
        'productos':productos,
        'datos_factura':datos_factura,
        }
    # return redirect("Tienda", datos_factura.pk)
    return render(request, 'facturacion/tienda.html', context)

def agregar_producto(request, producto_id):

    carrito = Carrito(request)
    producto = Insumo.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("Tienda", producto.pk)

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Insumo.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("Tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Insumo.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("Tienda",producto.pk)

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("clean_shop")



def guardar_carrito(request):
    carrito = Carrito(request)
    carrito.guardar_carrito()
    return redirect("generar_factura",)






def tiendas(request):
    #return HttpResponse("Hola Pythonizando")
    productos = Insumo.objects.all()
    return render(request, "facturacion/tienda.html", {'productos':productos})


def carrito(request,pk):
    factura = Compras.objects.get(id= pk)
    usuario = factura.filter(factura_id=factura.usuario,)
    vehiculo = factura.filter(factura_id=factura.vehiculo)
    
    print (factura)
    print (usuario)
    print (vehiculo)
    
    
    context ={
         'usuario':usuario,
         'factura':factura,
         'vehiculo': vehiculo,
    }
    return render(request, "facturacion/ver.html",context)