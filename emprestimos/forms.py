from django import forms
from .models import Emprestimo

class EmprestimoModelForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['pessoa', 'reserva']
        widgets = {
            'inicio': forms.DateTimeInput(attrs={'type': 'datetime-local' ,'class': 'form-control'}),
        }

        error_messages = {
            'inicio': {'required': 'O código do prédio é um campo obrigatório'},
            'pessoa': {'required': 'O código do prédio é um campo obrigatório'},
            'chave': {'required': 'A chave é um campo obrigatório'},
        }

class EmprestimoFimModelForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['fim']
        widgets = {
            'fim': forms.DateTimeInput(attrs={'type': 'datetime-local' ,'class': 'form-control'}),
        }