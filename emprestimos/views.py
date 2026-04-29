from django.contrib import messages
from django.contrib.messages import SUCCESS
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import render

from chave.models import Chave
from reservas.models import Reserva
from .forms import EmprestimoModelForm, EmprestimoFimModelForm, \
    EmprestimoReservaModelForm
from predios.models import Predio
from .models import Emprestimo


# Create your views here.
class EmprestimosView(ListView):
    model = Emprestimo
    template_name = 'emprestimos.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(EmprestimosView, self).get_queryset()
        if buscar:
            return qs.filter(codigo__icontains=buscar).exclude(fim__isnull=True)

        if qs.count() == 0:
            return messages.info(self.request,'Não existem empréstimos ativos!')
        else:
            return qs.exclude(fim__isnull=False)

class EmprestimoAddView(SuccessMessageMixin, CreateView):
    model = Emprestimo
    form_class = EmprestimoModelForm
    template_name = 'emprestimo_form.html'
    success_url = reverse_lazy('emprestimos')
    success_message = 'Empréstimo feito com sucesso'

    def form_valid(self, form):
        formulario = form.save(commit=False)
        chave_id = self.kwargs.get('pk')
        chave = Chave.objects.get(pk=chave_id)
        chave.disponivel = False
        chave.save()

        formulario.chave = chave
        formulario.save()

        return super().form_valid(form)



class EmprestimoReservaAddView(SuccessMessageMixin, CreateView):
    model = Emprestimo
    form_class = EmprestimoReservaModelForm
    template_name = 'emprestimo_form.html'
    success_url = reverse_lazy('emprestimos')
    success_message = 'Empréstimo feito com sucesso'

    def form_valid(self, form):
        formulario = form.save(commit=False)
        reserva_id = self.kwargs.get('pk')
        reserva = Reserva.objects.get(pk=reserva_id)
        formulario.reserva = reserva
        formulario.chave = reserva.chave
        formulario.pessoa = reserva.pessoa
        formulario.inicio = timezone.now()
        reserva.ativo = False
        reserva.save()
        formulario.save()

        return super().form_valid(form)

class EmprestimoUpdateView(SuccessMessageMixin, UpdateView):
    model = Emprestimo
    form_class = EmprestimoFimModelForm
    template_name = 'emprestimo_form.html'
    success_url = reverse_lazy('emprestimos')
    success_message = 'Emprestimo alterado com sucesso'

    def form_valid(self, form):
        formulario = form.save(commit=False)
        emprestimo_id = self.kwargs.get('pk')
        emprestimo = Emprestimo.objects.get(pk=emprestimo_id)
        emprestimo.fim = timezone.now()
        print(timezone.now())
        emprestimo.save()
        chave_id = emprestimo.chave.pk
        chave = Chave.objects.get(pk=chave_id)
        chave.disponivel = True
        chave.save()
        return super().form_valid(form)