from django.urls import path

from .views import buscar,busqueda_expediente,inicio, loginView

from .views import AdministrativoList,AdministrativoCreate,AdministrativoUpdate,AdministrativoDelete,AdministrativoDetail
from .views import MedicoList,MedicoCreate,MedicoUpdate,MedicoDelete,MedicoDetail
from .views import EnfermeroList,EnfermeroCreate,EnfermeroUpdate,EnfermeroDelete,EnfermeroDetail
from .views import PacienteList,PacienteCreate,PacienteUpdate,PacienteDelete,PacienteDetail

urlpatterns = [
    path("",inicio , name="Inicio" ),  
    #url busqueda
    path("busqueda_expediente/", busqueda_expediente, name="busqueda_expediente"),
    path("buscar/", buscar, name="buscar"),
    #url CRUD adminintrativo
    path('listaadministrativo/', AdministrativoList.as_view(), name="ListaAdministrativo"),
    path('detalleadministrativo/<pk>', AdministrativoDetail.as_view(), name="DetalleAdministrativo"),
    path('creaadministrativo/', AdministrativoCreate.as_view(), name="CreaAdministrativos"),
    path('actualizaradministrativo/<pk>', AdministrativoUpdate.as_view(), name="ActualizaAdministrativo"),
    path('eliminaradministrativo/<pk>', AdministrativoDelete.as_view(), name="EliminaAdministrativo"),
     #url CRUD Medico
    path('listaMedico/', MedicoList.as_view(), name="ListaMedico"),
    path('detallemedico/<pk>', MedicoDetail.as_view(), name="DetalleMedico"),
    path('creamedico/', MedicoCreate.as_view(), name="CreaMedico"),
    path('actualizarmedico/<pk>', MedicoUpdate.as_view(), name="ActualizaMedico"),
    path('eliminarmedico/<pk>', MedicoDelete.as_view(), name="EliminaMedico"),
    #url CRUD Enfermero
    path('listaEnfermero/', EnfermeroList.as_view(), name="ListaEnfermero"),
    path('detalleEnfermero/<pk>', EnfermeroDetail.as_view(), name="DetalleEnfermero"),
    path('creaEnfermero/', EnfermeroCreate.as_view(), name="CreaEnfermero"),
    path('actualizarEnfermero/<pk>', EnfermeroUpdate.as_view(), name="ActualizaEnfermero"),
    path('eliminarEnfermero/<pk>', EnfermeroDelete.as_view(), name="EliminaEnfermero"),
    #url CRUD Paciente
    path('listaPaciente/', PacienteList.as_view(), name="ListaPaciente"),
    path('detallePaciente/<pk>', PacienteDetail.as_view(), name="DetallePaciente"),
    path('creaPaciente/', PacienteCreate.as_view(), name="CreaPaciente"),
    path('actualizarPaciente/<pk>', PacienteUpdate.as_view(), name="ActualizaPaciente"),
    path('eliminarPaciente/<pk>', PacienteDelete.as_view(), name="EliminaPaciente"),
    #url CRUD Login
    path("login/", loginView, name='Login'),
]

