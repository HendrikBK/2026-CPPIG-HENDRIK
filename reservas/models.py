from django.db import models
from pessoas.models import Pessoa
from salas.models import Sala


# Create your models here.
class Reserva(models.Model):
    inicio = models.DateTimeField()
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT)
    sala = models.ForeignKey(Sala, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"

    def __str__(self):
        return str(self.inicio) + "-" + str(self.pessoa) + "-" + str(self.sala)