from django.urls import path
from chave.views import ChaveView, ChaveDeleteView, ChavePredioAddView

urlpatterns = [
    path('chaves', ChaveView.as_view(), name='chaves'),
    path('<int:pk>/chave/adicionar/', ChavePredioAddView.as_view(), name='chave_adicionar'),
    path('<int:pk>/chave/apagar/', ChaveDeleteView.as_view(),
         name='chave_apagar'),
]