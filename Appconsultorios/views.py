from django.http import HttpResponse
from django.shortcuts import render
from .models import Medico, Enfermero, Paciente, Administrativo
# Create your views here.

#def de modelos
def medico(request, nombre, apellido, especialidad, matricula):
    medico = Medico(nombre=nombre, apellido=apellido, especialidad=especialidad, matricula=matricula)
    medicos.save()

def administrativo(request, nombre, apellido, legajo):
    administrativo = Administrativo(nombre=nombre, apellido=apellido, legajo=legajo)
    administrativo.save()

def enfermero(request, nombre, apellido, matricula):
    enfermero = Enfermero(nombre=nombre, apellido=apellido, matricula=matricula)
    enfermero.save()

def paciente(request, nombre, apellido, fecha_nacimiento, tratamiento, expediente):
    paciente = Paciente(nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento, tratamiento=tratamiento, expediente=expediente)
    paciente.save()



#def html
def inicio(request):
    return render(request,'inicio.html')

def administrativos(request):
    lista=Administrativo.objects.all
    return render(request,'administrativos.html', {'lista_administrativos':lista})

def medicos(request):
    lista=Medico.objects.all
    return render(request, 'medicos.html',{'lista_medicos': lista})

def enfermeros(request):
    lista=Enfermero.objects.all
    return render(request, 'enfermeros.html', {'lista_enfermeros':lista})

def pacientes(request):
    lista=Paciente.objects.all
    return render(request, 'pacientes.html', {'lista_pacientes':lista})

