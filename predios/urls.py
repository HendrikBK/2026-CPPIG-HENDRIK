from django.urls import path
from predios.views import PrediosView, PredioDeleteView, PredioUpdateView, \
    PredioAddView

urlpatterns = [
    path('predios', PrediosView.as_view(), name='predios'),
    path('predio/adicionar/', PredioAddView.as_view(), name='predio_adicionar'),
    path('<int:pk>/predio/editar/', PredioUpdateView.as_view(), name='predio_editar'),
    path('<int:pk>/predio/apagar/', PredioDeleteView.as_view(),
         name='predio_apagar'),
]