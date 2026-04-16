from django.contrib import messages
from django.contrib.messages import SUCCESS
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .forms import ReservaModelForm
from predios.models import Predio
from .models import Reserva


# Create your views here.
class ReservasView(ListView):
    model = Reserva
    template_name = 'reservas.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(ReservasView, self).get_queryset()
        if buscar:
            return qs.filter(codigo__icontains=buscar)

        if qs.count() == 0:
            return messages.info(self.request,'Não existem reservas cadastradas!')
        else:
            return qs

class ReservaAddView(SuccessMessageMixin, CreateView):
    model = Reserva
    form_class = ReservaModelForm
    template_name = 'reserva_form.html'
    success_url = reverse_lazy('reservas')
    success_message = 'Reserva feita com sucesso'

class ReservaUpdateView(SuccessMessageMixin, UpdateView):
    model = Reserva
    form_class = ReservaModelForm
    template_name = 'reserva_form.html'
    success_url = reverse_lazy('reservas')
    success_message = 'Reserva alterada com sucesso'

class ReservaDeleteView(SuccessMessageMixin, DeleteView):
    model = Reserva
    template_name = 'reserva_apagar.html'
    success_url = reverse_lazy('reservas')
    sucess_message = 'Reserva apagada com sucesso'