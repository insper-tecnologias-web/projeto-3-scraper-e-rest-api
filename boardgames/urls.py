from django.urls import path

from . import views

urlpatterns = [
    path('', views.api_index, name='index'), # Redirecionar para a documentação
    path('rank',views.api_rank,name='rank'),
    path('rank/<int:id>/',views.api_rank_id,name='rank_id'),
    path('nome?',views.api_name,name='name'),
    path('random',views.api_random,name='random'),


]