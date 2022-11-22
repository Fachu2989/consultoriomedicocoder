from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Administrativo(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    legajo = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.legajo}"
class Medico(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50)
    matricula = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.especialidad} - {self.matricula}"

class Enfermero(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    matricula = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.matricula}"

class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    expediente = models.IntegerField()
    tratamiento = models.CharField(max_length=50)
    

    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.expediente} - {self.tratamiento}"

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='avatares', null=True, blank=True)


