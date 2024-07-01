from django.shortcuts import render, redirect
from .models import Estudiante
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')

def integrantes(request):
    return render(request, 'integrantes.html')

def saludo(request):
    return render(request, 'saludo.html')

def estudiantes(request):
    estLis = Estudiante.objects.all()
    return render(request, 'estudiantes.html', {"estudiantes": estLis})

def crear_estudiante(request):
    return render(request, 'crear_estudiante.html')

def registrar_estudiante(request):
    codigo = request.POST['codigo']
    dni = request.POST['dni']
    nombre = request.POST['nombre']
    apepat = request.POST['apepat']
    apemat = request.POST['apemat']
    direccion = request.POST['direccion']
    telefono = request.POST['telefono']
    estado = request.POST['estado']
    estudiante = Estudiante.objects.create(
        codigo=codigo, dni=dni, nombre=nombre, apepat=apepat, apemat=apemat, direccion= direccion, telefono = telefono, estado =estado)
    return redirect('/estudiantes/')

