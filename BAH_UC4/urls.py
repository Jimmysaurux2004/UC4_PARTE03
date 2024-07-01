"""
URL configuration for BAH_UC4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from miapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index, name = "index"),
    path('cursos/', views.integrantes, name = "integrantes"),
    path('saludo/', views.saludo, name = "saludo"),
    path('registrar_estudiante/', views.registrar_estudiante, name = "registrar_estudiante"),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('crear_estudiante/', views.crear_estudiante, name='crear_estudiante'),
]