from django.shortcuts import render
from django.views import View
from Alimento.models import Alimentos
from Alimento.serializador import *
from Artesanal.serializador import *
from Productos.serializador import *

class LandingPage(View):    #Aplica la misma lógica que el 'APIView' => GET,POST, PUT, ...
    templates = ['index.html']
    def get(self, request):
        return render(request, self.templates[0], {})
    def post(self, request):
        #Aplicamos lógica del login
        pass

class productos(View):    #Aplica la misma lógica que el 'APIView' => GET,POST, PUT, ...
    templates = ['products.html']
    def get(self, request):
        productos = Productos.objects.all()
        alS = Serialpersonal(productos, many=True)
        return render(request, self.templates[0], {'productos':alS.data})

    def post(self, request):
        #Aplicamos lógica del login
        pass

class blog(View):    #Aplica la misma lógica que el 'APIView' => GET,POST, PUT, ...
    templates = ['blog.html']
    def get(self, request):
        return render(request, self.templates[0], {})
    def post(self, request):
        #Aplicamos lógica del login
        pass

class single(View):    #Aplica la misma lógica que el 'APIView' => GET,POST, PUT, ...
    templates = ['contacto.html']
    def get(self, request):
        return render(request, self.templates[0], {})
    def post(self, request):
        #Aplicamos lógica del login
        pass

class alimentov(View):    #Aplica la misma lógica que el 'APIView' => GET,POST, PUT, ...
    templates = ['Alimentos.html']
    def get(self, request):
        alimentos = Alimentos.objects.all()
        alS = Serialalimento(alimentos, many=True)
        return render(request, self.templates[0], {'alimentos':alS.data})

    def post(self, request):
        #Aplicamos lógica del login
        pass

class artesaniasv(View):    #Aplica la misma lógica que el 'APIView' => GET,POST, PUT, ...
    templates = ['Artesanias.html']
    def get(self, request):
        artesa = Productosartesanal.objects.all()
        alS = Serialartesanias(artesa, many=True)
        return render(request, self.templates[0], {'artesa':alS.data})
    def post(self, request):
        #Aplicamos lógica del login
        pass