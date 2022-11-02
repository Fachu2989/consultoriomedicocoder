from django.urls import path

from .views import inicio,administrativos,medicos,enfermeros,pacientes

urlpatterns = [
    path("",inicio , name="Inicio" ),
    path('administrativos/',administrativos,name="administrativos"),
    path('medicos/', medicos,name="medicos"),
    path('enfermeros/', enfermeros,name="enfermeros"),
    path('pacientes/', pacientes, name="pacientes"),
]
