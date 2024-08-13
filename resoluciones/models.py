from django.db import models
from django.contrib.postgres.search import SearchQueryField

# Create your models here.

class Resoluciones(models.Model):
    class Origen(models.TextChoices):
        PROCURADOR = 'PTN', 'Procurador'
        SUBPROCURADOR = 'SPTN', 'SubProcurador'

    numero = models.IntegerField()
    fecha = models.DateField()
    sumario = models.CharField(max_length=500)
    fecha_publicacion = models.DateField()
    observaciones = models.CharField(max_length=500)
    origen = models.CharField(
        max_length=4,
        choices= Origen.choices,
        default=Origen.PROCURADOR)
    activo = models.BooleanField(default=True)
    tsbuscar = models.SmallIntegerField(null=True, blank=True)

    class Meta:
        db_table = 'resoluciones'

    def __str__(self):
        return f" Numero: {self.numero} - Fecha: {self.fecha} - Sumario: {self.sumario} - Observaciones: {self.observaciones}"

