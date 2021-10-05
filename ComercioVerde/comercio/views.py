from django.shortcuts import render
from django.views import View

class LandingPage(View):    #Aplica la misma lógica que el 'APIView' => GET,POST, PUT, ...
    templates = ['index.html']
    def get(self, request):
        return render(request, self.templates[0], {})
    def post(self, request):
        #Aplicamos lógica del login
        pass
