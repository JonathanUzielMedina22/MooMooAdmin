from django.db import models
from django.contrib.auth.models import User

class Ganado_Vacuno (models.Model):
    codigo_arete = models.CharField(max_length=25, verbose_name="Código de Arete")
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento (Año-Mes-Día)")
    fecha_compra = models.DateField(verbose_name="Fecha de compra (Año-Mes-Día)")
    dueno = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Dueño")
    raza = models.CharField(max_length=25)
    color = models.CharField(max_length=25)
    sexo = models.CharField(max_length=25)
    lugar_origen = models.CharField(max_length=100, verbose_name="Lugar de origen")
    precio_por_kilo = models.FloatField(verbose_name="Precio por kilogramo")
    estaVivo = models.BooleanField(verbose_name="¿Está vivo(a)?")
    agregado = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion_datos = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.codigo_arete + " (" + self.raza + " - " + self.color + ")"