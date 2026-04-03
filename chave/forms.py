from django import forms

from predios.models import Predio
from .models import Chave, ChavePredio

class ChavePredioModelForm(forms.ModelForm):
    class Meta:
        model = ChavePredio
        fields = []

        error_messages = {
            'numero': {'required': 'O número da salas é um campo obrigatório'},
        }

    # def save(self, commit=True):
    #     predio = Predio.objects.get(pk=self.kwargs['pk'])
    #     self.instance.predio = predio
    #     print("teste")
    #     print(self.cleaned_data)
    #     return super().save(commit)