from django.contrib import messages
from django.contrib.messages import SUCCESS
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .forms import PredioModelForm
from predios.models import Predio


# Create your views here.
class PrediosView(ListView):
    model = Predio
    template_name = 'predios.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(PrediosView, self).get_queryset()
        if buscar:
            return qs.filter(nome__icontains=buscar)

        if qs.count() == 0:
            return messages.info(self.request,'Não existem prédios cadastrados!')
        else:
            return qs

class PredioAddView(SuccessMessageMixin, CreateView):
    model = Predio
    form_class = PredioModelForm
    template_name = 'predio_form.html'
    success_url = reverse_lazy('predios')
    success_message = 'Prédio cadastrado com sucesso'


    def form_valid(self, form):
        form.save(commit=False)
        form.instance.codigo = form.instance.codigo.upper()
        return super().form_valid(form)


class PredioUpdateView(SuccessMessageMixin, UpdateView):
    model = Predio
    form_class = PredioModelForm
    template_name = 'predio_form.html'
    success_url = reverse_lazy('predios')
    success_message = 'Prédio alterado com sucesso'

class PredioDeleteView(SuccessMessageMixin, DeleteView):
    model = Predio
    template_name = 'predio_apagar.html'
    success_url = reverse_lazy('predios')
    sucess_message = 'Prédio apagado com sucesso'