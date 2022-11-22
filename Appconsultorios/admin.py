from django.contrib import admin
from .models import Paciente,Enfermero,Medico,Administrativo,Avatar
# Register your models here.
admin.site.register(Administrativo)
admin.site.register(Medico)
admin.site.register(Enfermero)
admin.site.register(Paciente)

admin.site.register(Avatar)