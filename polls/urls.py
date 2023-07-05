from django.urls import path
from . import views

app_name = 'polls' #nombre de la app para diferenciar los names de los urls distintas apps.
urlpatterns = [
    path('', views.IndexView.as_view(), name='indice'),
    path('<int:pk>/', views.DetailQuestionView.as_view(), name='detalle'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='resultados'),
    path('<int:question_id>/vote/', views.vote, name='votos'),
]