from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Game
from .serializers import GameSerializer

# Create your views here.
@api_view(['GET'])
def api_rank(request): #APENAS LAYOUT MONTADO
    try:
        game = Game.objects.order_by('rank')[0:100] #equivalente a página 1
    except game.DoesNotExist:
        raise Http404()
    serialized_game = GameSerializer(game)
    return Response(serialized_game.data)

@api_view(['GET'])
def api_rank_id(request,rank_id): #APENAS LAYOUT MONTADO
    try:
        game = Game.objects.order_by('rank')[rank_id+1]
    except game.DoesNotExist:
        raise Http404()
    return Response(game)

@api_view(['GET'])
def api_name(request): #APENAS LAYOUT MONTADO
    try:
        game = Game.objects.all()
    except game.DoesNotExist:
        raise Http404()
    serialized_game = GameSerializer(game)
    return Response(serialized_game)

@api_view(['GET'])
def api_random(request): #APENAS LAYOUT MONTADO
    try:
        game = Game.objects.all()
    except game.DoesNotExist:
        raise Http404()
    serialized_game = GameSerializer(game)
    return Response(serialized_game)

@api_view(['GET'])
def api_category(request): #APENAS LAYOUT MONTADO
    try:
        game = Game.objects.all()
    except game.DoesNotExist:
        raise Http404()
    serialized_game = GameSerializer(game)
    return Response(serialized_game)