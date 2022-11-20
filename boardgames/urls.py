from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/rank',views.rank,name='rank'),
    path('/rank/<int:id>/',views.rank,name='rank_id'),
    path('/nome?',views.rank,name='name'),
    path('/random',views.rank,name='random'),
    path('/category?',views.rank,name='category'),

]