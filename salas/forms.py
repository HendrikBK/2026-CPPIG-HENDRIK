from django import forms
from .models import Sala

class SalaModelForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ['predio', 'numero']

        error_messages = {
            'numero': {'required': 'O número da salas é um campo obrigatório'},
        }