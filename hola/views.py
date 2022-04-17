from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hola(request):
    return HttpResponse("Hola Mundo!")

# def chao(request, nombre):
#     return HttpResponse(f"Chao {nombre}")

def saludoHTML(request):
    return render(request, 'hola/index.html')

def saludoVariableHTML(request, nombre):
    context = {'name' : nombre}
    return render(request, 'hola/saludar.html', context)