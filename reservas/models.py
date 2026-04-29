from django.db import models

from chave.models import Chave
from pessoas.models import Pessoa


# Create your models here.
class Reserva(models.Model):
    inicio = models.DateTimeField()
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT)
    chave = models.ForeignKey(Chave, on_delete=models.PROTECT)
    ativo = models.BooleanField("Ativo", default=True)

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"

    def __str__(self):
        return str(self.inicio) + "-" + str(self.pessoa) + "-" + str(self.chave)