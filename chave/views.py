from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.contrib.messages import SUCCESS
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render

from predios.models import Predio
from salas.models import Sala
from .forms import ChavePredioModelForm, ChaveSalaModelForm
from chave.models import Chave, ChavePredio, ChaveSala


# Create your views here.
class ChaveView(ListView):
    model = Chave
    template_name = 'chaves.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(ChaveView, self).get_queryset()
        if buscar:
            return qs.filter(codigo__icontains=buscar)

        if qs.count() == 0:
            return messages.info(self.request,'Não existem chaves cadastrados!')
        else:
            return qs

class ChavePredioAddView(SuccessMessageMixin, CreateView):
    model = ChavePredio
    form_class = ChavePredioModelForm
    template_name = 'chave_predio_form.html'
    success_url = reverse_lazy('chaves')
    success_message = 'Chave cadastrada com sucesso'


    def form_valid(self, form):
        form.save(commit=False)
        predio_id = self.kwargs.get('pk')
        predio = Predio.objects.get(pk=predio_id)

        if ChavePredio.objects.filter(predio=predio_id).count() == 0:
            form.instance.numero = 1
        else:
            i = ChavePredio.objects.filter(predio=predio_id).count() - 1
            form.instance.numero = int(ChavePredio.objects.all()[i].numero) + 1

        form.instance.predio = predio
        form.instance.codigo = str(form.instance.predio) + "-" + str(form.instance.numero)
        return super().form_valid(form)

class ChaveSalaAddView(SuccessMessageMixin, CreateView):
    model = ChaveSala
    form_class = ChaveSalaModelForm
    template_name = 'chave_sala_form.html'
    success_url = reverse_lazy('chaves')
    success_message = 'Chave cadastrada com sucesso'


    def form_valid(self, form):
        form.save(commit=False)
        sala_id = self.kwargs.get('pk')
        sala = Sala.objects.get(pk=sala_id)

        if ChaveSala.objects.filter(sala=sala_id).count() == 0:
            form.instance.numero = 1
        else:
            i = ChaveSala.objects.filter(sala=sala_id).count() - 1
            form.instance.numero = int(ChaveSala.objects.all()[i].numero) + 1

        form.instance.sala = sala
        form.instance.codigo = str(form.instance.sala) + "-" + str(form.instance.numero)
        return super().form_valid(form)
class ChaveDeleteView(SuccessMessageMixin, DeleteView):
    model = Chave
    template_name = 'chave_predio_apagar.html'
    success_url = reverse_lazy('chaves')
    sucess_message = 'Chave apagada com sucesso'