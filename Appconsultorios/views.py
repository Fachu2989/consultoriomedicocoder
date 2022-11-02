from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Medico, Enfermero, Paciente, Administrativo
from .form import AdministrativoFormulario,EnfermeroFormulario,MedicoFormulario,PacienteFormulario
# Create your views here.

#def de modelos
def medico(request, nombre, apellido, especialidad, matricula):
    medico = Medico(nombre=nombre, apellido=apellido, especialidad=especialidad, matricula=matricula)
    medico.save()

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

#formulario

def administrativoFormulario(request):

    if request.method =="POST":
        mi_formulario= AdministrativoFormulario(request.POST)
        if mi_formulario.is_valid():
            data=mi_formulario.cleaned_data
            administrativo=Administrativo(nombre=data["nombre"],apellido=data["apellido"],legajo=data["legajo"])
            administrativo.save()
            return redirect("administrativos")
    else: 
        mi_formulario=AdministrativoFormulario()
     
    return render(request, "administrativoFormulario.html",{'mi_formulario': mi_formulario})

def enfermeroFormulario(request):

    if request.method =="POST":
        mi_formulario= EnfermeroFormulario(request.POST)
        if mi_formulario.is_valid():
            data=mi_formulario.cleaned_data
            enfermero=Administrativo(nombre=data["nombre"],apellido=data["apellido"],legajo=data["legajo"])
            enfermero.save()
            return redirect("enfermeros")
    else: 
        mi_formulario=EnfermeroFormulario()
     
    return render(request, "enfermeroFormulario.html",{'mi_formulario': mi_formulario})

def medicoFormulario(request):

    if request.method =="POST":
        mi_formulario= MedicoFormulario(request.POST)
        if mi_formulario.is_valid():
            data=mi_formulario.cleaned_data
            medico=Administrativo(nombre=data["nombre"],apellido=data["apellido"],legajo=data["legajo"],especialidad=data["especialidad"])
            medico.save()
            return redirect("medicos")
    else: 
        mi_formulario=MedicoFormulario()
     
    return render(request, "medicoFormulario.html",{'mi_formulario': mi_formulario})

def pacienteFormulario(request):

    if request.method =="POST":
        mi_formulario= PacienteFormulario(request.POST)
        if mi_formulario.is_valid():
            data=mi_formulario.cleaned_data
            paciente=Paciente(nombre=data["nombre"],apellido=data["apellido"],legajo=data["legajo"])
            paciente.save()
            return redirect("pacientes")
    else: 
        mi_formulario=PacienteFormulario()
     
    return render(request, "pacienteFormulario.html",{'mi_formulario': mi_formulario})