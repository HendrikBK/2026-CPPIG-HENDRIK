from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Pessoa(models.Model):
    cpf = models.CharField("CPF", max_length=11, help_text="Matrícula da pessoa", unique=True, validators=[RegexValidator(regex=r'\d{11}',)])
    nome = models.CharField("Nome", max_length=100, help_text="Nome da pessoa")

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

    def __str__(self):
        return self.cpf