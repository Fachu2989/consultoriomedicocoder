from django.urls import path

from .views import buscar,busqueda_medico,inicio,administrativos,medicos,enfermeros,pacientes,administrativoFormulario,medicoFormulario,pacienteFormulario,enfermeroFormulario

urlpatterns = [
    path("",inicio , name="Inicio" ),
    path('administrativos/',administrativos,name="administrativos"),
    path('medicos/', medicos,name="medicos"),
    path('enfermeros/', enfermeros,name="enfermeros"),
    path('pacientes/', pacientes, name="pacientes"),
    #url formulario
    path('administrativoFormulario/',administrativoFormulario, name="administrativoFormulario"),
    path('medicoFormulario/',medicoFormulario, name="medicoFormulario"),
    path('pacienteFormulario/',pacienteFormulario, name="pacienteFormulario"),
    path('enfermeroFormulario/',enfermeroFormulario, name="enfermeroFormulario"),
    #url busqueda
    path("busqueda_medico/", busqueda_medico, name="busqueda_medico"),
    path("buscar/", buscar, name="buscar"),
]
