from django.db import models

from django.db import models
from django.core.validators import RegexValidator

from predios.models import Predio


# Create your models here.
class Sala(models.Model):
    predio = models.ForeignKey(Predio,on_delete=models.CASCADE)
    numero = models.CharField("Número", max_length=3, help_text="Número da Sala", validators=[RegexValidator(regex=r'\b[1-9]{1}[0-9]{1}[1-9]{1}\b',)])
    nome = models.CharField(max_length=6, unique=True)

    class Meta:
        verbose_name = "Sala"
        verbose_name_plural = "Salas"

    def __str__(self):
        return self.nome