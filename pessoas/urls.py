from django.urls import path
from pessoas.views import PessoasView, PessoaDeleteView, PessoaUpdateView, \
    PessoaAddView

urlpatterns = [
    path('pessoas', PessoasView.as_view(), name='pessoas'),
    path('pessoa/adicionar/', PessoaAddView.as_view(), name='pessoa_adicionar'),
    path('<int:pk>/pessoa/editar/', PessoaUpdateView.as_view(), name='pessoa_editar'),
    path('<int:pk>/pessoa/apagar/', PessoaDeleteView.as_view(),
         name='pessoa_apagar'),
]