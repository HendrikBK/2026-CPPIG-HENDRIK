from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.contrib.messages import SUCCESS
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .forms import SalaModelForm
from salas.models import Sala


# Create your views here.
class SalaView(ListView):
    model = Sala
    template_name = 'salas.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(SalaView, self).get_queryset()
        if buscar:
            return qs.filter(nome__icontains=buscar)

        if qs.count() == 0:
            return messages.info(self.request,'Não existem salas cadastrados!')
        else:
            return qs

class SalaAddView(SuccessMessageMixin, CreateView):
    model = Sala
    form_class = SalaModelForm
    template_name = 'sala_form.html'
    success_url = reverse_lazy('salas')
    success_message = 'Sala cadastrada com sucesso'


    def form_valid(self, form):
        form.save(commit=False)
        form.instance.nome = str(form.instance.predio) + str(form.instance.numero)
        return super().form_valid(form)


class SalaUpdateView(SuccessMessageMixin, UpdateView):
    model = Sala
    form_class = SalaModelForm
    template_name = 'sala_form.html'
    success_url = reverse_lazy('salas')
    success_message = 'Sala alterada com sucesso'

class SalaDeleteView(SuccessMessageMixin, DeleteView):
    model = Sala
    template_name = 'sala_apagar.html'
    success_url = reverse_lazy('salas')
    sucess_message = 'Sala apagada com sucesso'