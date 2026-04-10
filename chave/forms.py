from django import forms

from predios.models import Predio
from .models import ChavePredio, ChaveSala


class ChavePredioModelForm(forms.ModelForm):
    class Meta:
        model = ChavePredio
        fields = []

        error_messages = {
            'codigo': {'required': 'O código do prédio é um campo obrigatório'},
        }

class ChaveSalaModelForm(forms.ModelForm):
    class Meta:
        model = ChaveSala
        fields = []

        error_messages = {
            'numero': {'required': 'O número da sala é um campo obrigatório'},
        }