from django import forms
from .models import Predio

class PredioModelForm(forms.ModelForm):
    class Meta:
        model = Predio
        fields = '__all__'

        error_messages = {
            'codigo': {'required': 'O código do prédio é um campo obrigatório'},
        }