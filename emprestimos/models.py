from django.utils import timezone

from django.db import models
from chave.models import Chave
from pessoas.models import Pessoa
from reservas.models import Reserva


# Create your models here.
class Emprestimo(models.Model):
    inicio = models.DateTimeField(default=timezone.now)
    fim = models.DateTimeField(null=True, blank=True)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT)
    chave = models.ForeignKey(Chave, on_delete=models.PROTECT)
    reserva = models.ForeignKey(Reserva,on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name = "Empréstimo"
        verbose_name_plural = "Empréstimos"

    def __str__(self):
        return str(self.inicio) + "-" + str(self.pessoa) + "-" + str(self.chave)