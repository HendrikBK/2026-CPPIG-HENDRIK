from django import forms
from .models import Pessoa

class PessoaModelForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'

        error_messages = {
            'cpf': {'required': 'O CPF é obrigatório'},
            'nome': {'required': 'O nome do usuário é obigatório'},
        }