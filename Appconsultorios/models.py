from django.db import models

# Create your models here.
class Administrativo(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    legajo = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.nombre} - {self.camada} - {self.legajo}"

class Medico(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.nombre} - {self.apellido} - {self.especialidad}"

class Enfermero(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    legajo = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.nombre} - {self.apellido} - {self.legajo}"

class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    expediente = models.IntegerField()
    tratamiento = models.CharField(max_length=50)
    nacimiento = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self) -> str:
        return f"{self.nombre} - {self.apellido} - {self.nacimiento} - {self.expediente} - {self.tratamiento}"



