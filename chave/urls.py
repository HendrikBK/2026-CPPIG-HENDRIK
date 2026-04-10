from django.urls import path
from chave.views import ChaveView, ChaveDeleteView, ChavePredioAddView, \
    ChaveSalaAddView

urlpatterns = [
    path('chaves', ChaveView.as_view(), name='chaves'),
    path('<int:pk>/chave_predio/adicionar/', ChavePredioAddView.as_view(), name='chave_predio_adicionar'),
    path('<int:pk>/chave_sala/adicionar/', ChaveSalaAddView.as_view(), name='chave_sala_adicionar'),
    path('<int:pk>/chave/apagar/', ChaveDeleteView.as_view(),
         name='chave_apagar'),
]