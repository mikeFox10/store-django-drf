from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
from core.models import Articulos
from core.forms import FormularioContacto
# Create your views here.

def busqueda_productos(request):
    return render(request, "busqueda_productos.html")

def buscar(request):

    if request.GET['prd']:
        mensaje = 'Articulo buscado: %r ' %request.GET['prd']
        if len(request.GET['prd']) > 20:
            mensaje ="Texto de búsqueda demasiado largo"
        else:
            articulos = Articulos.objects.filter(nombre__icontains=request.GET['prd'])
            return render(request, "resultados_busqueda.html", {'articulos':articulos, 'query':request.GET['prd']})
    else:
        mensaje='Debes ingresar el producto a buscar'

    return HttpResponse(mensaje)

def contacto(request):
    if request.method == "POST":
        miFormulario = FormularioContacto(request.POST)
        if miFormulario.is_valid():
            informacionForm=miFormulario.cleaned_data
            # send mail
            # obteniendo datos . informacionForm.get('email')
        return render(request, 'gracias_contacto.html')
    else:
        miFormulario = FormularioContacto()
        return render(request, "contacto.html", {"form": miFormulario})