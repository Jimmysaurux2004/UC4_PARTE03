from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')

def integrantes(request):
    return render(request, 'integrantes.html')

def saludo(request):
    return render(request, 'saludo.html')
