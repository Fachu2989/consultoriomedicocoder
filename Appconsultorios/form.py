from django import forms


class AdministrativoFormulario(forms.Form):
    nombre= forms.CharField()
    apellido= forms.CharField()
    legajo = forms.IntegerField()

class EnfermeroFormulario(forms.Form):
    nombre= forms.CharField()
    apellido= forms.CharField()
    matricula = forms.IntegerField()

class MedicoFormulario(forms.Form):
    nombre= forms.CharField()
    apellido= forms.CharField()
    especialidad = forms.CharField()
    matricula = forms.IntegerField()

class PacienteFormulario(forms.Form):
    nombre= forms.CharField()
    apellido= forms.CharField()
    tratamiento = forms.CharField()
    #nacimiento = forms.DateField(required=False)
    expediente = forms.IntegerField()