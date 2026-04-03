from django.db import models

from django.db import models
from django.core.validators import RegexValidator
from django.utils.timezone import override

from salas.models import Sala
from predios.models import Predio


# Create your models here.
class Chave(models.Model):
    codigo = models.CharField(max_length=9, unique=True)
    numero = models.CharField("Número", max_length=3, help_text="Número da Chave", validators=[RegexValidator(regex=r'\b[0-9]{2}\b',)])

    class Meta:
        verbose_name = "Chave"
        verbose_name_plural = "Chaves"

    def __str__(self):
        return self.codigo

class ChavePredio(Chave):
    predio = models.ForeignKey(Predio, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Chave de prédio"
        verbose_name_plural = "Chaves de prédios"


class ChaveSala(Chave):
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Chave de sala"
        verbose_name_plural = "Chaves de salas"