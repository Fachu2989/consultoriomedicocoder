from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Medico, Enfermero, Paciente, Administrativo

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
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
    paciente = Paciente(nombre=nombre, apellido=apellido, tratamiento=tratamiento, expediente=expediente)
    paciente.save()



#def Inicio
def inicio(request):
    return render(request,'inicio.html')

#busqueda

def busqueda_expediente(request):
    return render(request, 'busqueda_paciente.html')

def buscar(request):
    expediente_buscada= request.GET["expediente"]
    paciente= Paciente.objects.get(expediente=expediente_buscada)
    return render(request,'resultado_busqueda.html',{"paciente":paciente, "expediente": expediente_buscada})


#Crud administrativo
class AdministrativoList(ListView):

    model = Administrativo
    template_name = 'administrativo_list.html'
    context_object_name = "administrativos"

class AdministrativoDetail(DetailView):

    model = Administrativo
    template_name = 'administrativo_detail.html'
    context_object_name = "administrativo"

class AdministrativoCreate(CreateView):

    model = Administrativo
    template_name = 'administrativo_create.html'
    fields = ('__all__')
    success_url = '/consultorio/'

class AdministrativoUpdate(UpdateView):

    model = Administrativo
    template_name = 'administrativo_update.html'
    fields = ('__all__')
    success_url = '/consultorio/'

class AdministrativoDelete(DeleteView):

    model = Administrativo
    template_name = 'administrativo_delete.html'
    success_url = '/consultorio/'

#Crud medico
class MedicoList(ListView):

    model = Medico
    template_name = 'medico_list.html'
    context_object_name = "medicos"

class MedicoDetail(DetailView):

    model = Medico
    template_name = 'medico_detail.html'
    context_object_name = "medico"

class MedicoCreate(CreateView):

    model = Medico
    template_name = 'medico_create.html'
    fields = ('__all__')
    success_url = '/consultorio/'

class MedicoUpdate(UpdateView):

    model = Medico
    template_name = 'medico_update.html'
    fields = ('__all__')
    success_url = '/consultorio/'

class MedicoDelete(DeleteView):

    model = Medico
    template_name = 'medico_delete.html'
    success_url = '/consultorio/'

#Crud enfermero
class EnfermeroList(ListView):

    model = Enfermero
    template_name = 'enfermero_list.html'
    context_object_name = "enfermeros"

class EnfermeroDetail(DetailView):

    model = Enfermero
    template_name = 'enfermero_detail.html'
    context_object_name = "enfermero"

class EnfermeroCreate(CreateView):

    model = Enfermero
    template_name = 'enfermero_create.html'
    fields = ('__all__')
    success_url = '/consultorio/'

class EnfermeroUpdate(UpdateView):

    model = Enfermero
    template_name = 'enfermero_update.html'
    fields = ('__all__')
    success_url = '/consultorio/'

class EnfermeroDelete(DeleteView):

    model = Enfermero
    template_name = 'enfermero_delete.html'
    success_url = '/consultorio/'

#Crud paciente
class PacienteList(ListView):

    model = Paciente
    template_name = 'paciente_list.html'
    context_object_name = "pacientes"

class PacienteDetail(DetailView):

    model = Paciente
    template_name = 'paciente_detail.html'
    context_object_name = "paciente"

class PacienteCreate(CreateView):

    model = Paciente
    template_name = 'paciente_create.html'
    fields = ('__all__')
    success_url = '/consultorio/'

class PacienteUpdate(UpdateView):

    model = Paciente
    template_name = 'paciente_update.html'
    fields = ('__all__')
    success_url = '/consultorio/'

class PacienteDelete(DeleteView):

    model = Paciente
    template_name = 'paciente_delete.html'
    success_url = '/consultorio/'

#Crud login

def loginView(request):
    if request.method =="POST":
        mi_formulario= AuthenticationForm(request,data=request.POST)
        if mi_formulario.is_valid():
            data=mi_formulario.cleaned_data
            usuario=data["username"]
            psw=data["password"]
            user= authenticate(username=usuario, password=psw)
            if user:
                 login(request,user)
                 return render(request, "inicio.html",{'mensaje': f'bienvenido {usuario}'})
            else:
                return render(request, "inicio.html",{'mensaje': f'Error datos incorrectos'})
        
        return render(request, "inicio.html",{'mensaje': f'Error formulario invalido'})

    else: 
        mi_formulario=AuthenticationForm()
     
    return render(request, "login.html",{'mi_formulario': mi_formulario})

