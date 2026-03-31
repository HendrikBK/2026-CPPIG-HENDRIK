from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Predio(models.Model):
    codigo = models.CharField("Código", max_length=2, help_text="Código do prédio", unique=True, validators=[RegexValidator(regex=r'[A-Z]|[a-z]{1,2}',)])

    class Meta:
        verbose_name = "Prédio"
        verbose_name_plural = "Prédios"

    def __str__(self):
        return self.codigo