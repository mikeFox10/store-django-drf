from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from core import serializers, models
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


class HelloApiView(APIView):
    seralizer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        an_apiview = [
            'testing',
            'APIVIEW - Mayor control de la logica de la APP'
        ]
        return Response({'message': 'OK', "respuesta": an_apiview })

    def post(self, request):
        serializer = self.seralizer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = 'Hello ' + name
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    def put(self, request, pk=None):
        return Response({'method' :" PUT"})

class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        a_viewset = [
            "VIEW SET Use acctions list. crate retrieve, update",
            "menos control de la l'ogica"
        ]
        return Response({"mensaje": "OK", 'result': a_viewset})
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = 'Hello ' + name
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        return Response({'message': 'GET'})

class UserpProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()