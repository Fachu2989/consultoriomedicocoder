from django import forms
from .models import Paciente
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

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

# class PacienteFormulario(forms.Form):
#     nombre= forms.CharField()
#     apellido= forms.CharField()
#     tratamiento = forms.CharField()
#     expediente = forms.IntegerField()

class PacienteFormulario(forms.ModelForm):

    class Meta:
        model = Paciente 
        fields = ('__all__')
        widgets = {
            'nombre': forms.TextInput(
                attrs={    
                        'placeholder': 'Ingrese un nombre...'}
                       
            ),
            'apellido': forms.TextInput(
                attrs={    
                        'placeholder': 'Ingrese un apellido...'}
            )
        }

class UserEditForm(UserChangeForm):

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False 
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

def clean_password2(self):


    password2 = self.cleaned_data["password2"]
    if password2 != self.cleaned_data['password1']:
        raise forms.ValidationError('Las contraseñas no coinciden!')
    return password2