from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hola(request):
    return HttpResponse("Hola Mundo!")

def chao(request, nombre):
    return HttpResponse(f"Chao {nombre}")

def saludoHTML(request):
    return render(request, 'hola/index.html')