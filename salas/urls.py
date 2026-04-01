from django.urls import path
from salas.views import SalaView, SalaDeleteView, SalaUpdateView, \
    SalaAddView

urlpatterns = [
    path('salas', SalaView.as_view(), name='salas'),
    path('sala/adicionar/', SalaAddView.as_view(), name='sala_adicionar'),
    path('<int:pk>/sala/editar/', SalaUpdateView.as_view(), name='sala_editar'),
    path('<int:pk>/sala/apagar/', SalaDeleteView.as_view(),
         name='sala_apagar'),
]