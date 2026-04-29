from django import forms
from .models import Reserva

class ReservaModelForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['inicio', 'pessoa']
        widgets = {
            'inicio': forms.DateTimeInput(attrs={'type': 'datetime-local' ,'class': 'form-control'}),
        }

        error_messages = {
            'inicio': {'required': 'O código do prédio é um campo obrigatório'},
            'pessoa': {'required': 'O código do prédio é um campo obrigatório'},
            'sala': {'required': 'O código do prédio é um campo obrigatório'},
        }