from django.urls import path

from .views import AdministrativoList,AdministrativoCreate,AdministrativoUpdate,AdministrativoDelete,AdministrativoDetail, buscar,busqueda_expediente,inicio,administrativos,medicos,enfermeros,pacientes,administrativoFormulario,medicoFormulario,pacienteFormulario,enfermeroFormulario

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
    path("busqueda_expediente/", busqueda_expediente, name="busqueda_expediente"),
    path("buscar/", buscar, name="buscar"),
    #CRUD Administrativos
    path('listaAdministrativo', AdministrativoList.as_view(), name="ListaAdministrativo"),
    path('detalleAdministrativo/<pk>', AdministrativoDetail.as_view(), name="DetalleAdministrativo"),
    path('creaAdministrativo/', AdministrativoCreate.as_view(), name="CreaAdministrativo"),
    path('actualizarAdministrativo/<pk>', AdministrativoUpdate.as_view(), name="ActualizaAdministrativo"),
    path('eliminarAdministrativo/<pk>', AdministrativoDelete.as_view(), name="EliminaAdministrativo"),
]
