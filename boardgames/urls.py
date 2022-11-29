from django.urls import path

from . import views

urlpatterns = [
    path('', views.api_index, name='index'), # Redirecionar para a documentação
    path('rank',views.api_rank,name='rank'),
    path('rank/<int:rank_id>/',views.api_rank_id,name='rank_id'),
    path('name/<str:name>',views.api_name,name='name'),
    path('name',views.api_name_erro,name='name'),
    path('random',views.api_random,name='random'),
    path('year/<int:year>', views.api_year,name='year')


]