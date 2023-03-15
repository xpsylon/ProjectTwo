from django.urls import path
from . import views

app_name = 'polls' #nombre de la app para diferenciar los names de los urls distintas apps.
urlpatterns = [
    path('', views.index, name='indice'),
    path('<int:question_id>/', views.detail, name='detalle'),
    path('<int:question_id>/results/', views.results, name='resultados'),
    path('<int:question_id>/vote/', views.vote, name='votos'),
]