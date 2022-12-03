from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404, JsonResponse
from .models import Game
from .serializers import GameSerializer
import random


# Create your views here.
@api_view(['GET']) #/rank
def api_rank(request):

    try:
        games = Game.objects.all() #equivalente a página 1
    except games.DoesNotExist:
        raise Http404()
    serialized_game = GameSerializer(games,many=True)
    print(serialized_game)
    # return JsonResponse({"teste" : "data"})
    
    return Response(serialized_game.data)



@api_view(['GET'])
def api_rank_id(request,rank_id):
    print('esse aqui é o id que foi chamado: ' , rank_id) # 
    try:
        game = Game.objects.get(id=rank_id)
        print(game)
    except game.DoesNotExist:
        raise Http404()
    serialized_game = GameSerializer(game)
    #return JsonResponse({"game": "game"})
    return Response(serialized_game.data)

@api_view(['GET'])
def api_name(request,name):
    print(name)
    try:
        game = Game.objects.filter(name__startswith=name)
    except game.DoesNotExist:
        raise Http404()
    serialized_game = GameSerializer(game,many=True)
    return Response(serialized_game.data)

@api_view(['GET'])
def api_name_erro(request):
    string = 'É necessário colocar o um /nome, então a endpoint correta é: /name/<str:name>'
    return Response(string)

@api_view(['GET'])
def api_random(request):
    teste = random.randint(1,2000)
    try:
        game = Game.objects.get(id = teste)
    except game.DoesNotExist:
        raise Http404()
    serialized_game = GameSerializer(game)
    return Response(serialized_game.data)

@api_view(['GET'])
def api_index(request):
    try:
        game = Game.objects.all()
    except game.DoesNotExist:
        raise Http404()

    serialized_game = GameSerializer(game)
    return render(request, 'boardgames/index.html')

@api_view(['GET'])
def api_year(request,year):
    try:
        game = Game.objects.filter(year = year)
    except game.DoesNotExist:
        raise Http404()
    serialized_game = GameSerializer(game,many=True)
    return Response(serialized_game.data)