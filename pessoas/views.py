from django.contrib import messages
from django.contrib.messages import SUCCESS
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .forms import PessoaModelForm
from .models import Pessoa


# Create your views here.
class PessoasView(ListView):
    model = Pessoa
    template_name = 'pessoas.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(PessoasView, self).get_queryset()
        if buscar:
            return qs.filter(codigo__icontains=buscar)

        if qs.count() == 0:
            return messages.info(self.request,'Não existem pessoas cadastradas!')
        else:
            return qs

class PessoaAddView(SuccessMessageMixin, CreateView):
    model = Pessoa
    form_class = PessoaModelForm
    template_name = 'pessoa_form.html'
    success_url = reverse_lazy('pessoas')
    success_message = 'Pessoa cadastrada com sucesso'

class PessoaUpdateView(SuccessMessageMixin, UpdateView):
    model = Pessoa
    form_class = PessoaModelForm
    template_name = 'pessoa_form.html'
    success_url = reverse_lazy('pessoas')
    success_message = 'Pessoa alterada com sucesso'

class PessoaDeleteView(SuccessMessageMixin, DeleteView):
    model = Pessoa
    template_name = 'pessoa_apagar.html'
    success_url = reverse_lazy('pessoas')
    sucess_message = 'Pessoa apagada com sucesso'