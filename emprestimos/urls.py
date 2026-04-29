from django.urls import path

from emprestimos.views import EmprestimosView, EmprestimoAddView, \
    EmprestimoUpdateView, EmprestimoReservaAddView

urlpatterns = [
    path('emprestimos', EmprestimosView.as_view(), name='emprestimos'),
    path('<int:pk>/emprestimo/adicionar/', EmprestimoReservaAddView.as_view(), name='emprestimo_adicionar'),
    path('<int:pk>/emprestimo/editar/', EmprestimoUpdateView.as_view(), name='emprestimo_editar'),
]