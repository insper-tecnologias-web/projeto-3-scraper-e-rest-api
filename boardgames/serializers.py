from rest_framework import serializers
from .models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['name', 'rank', 'photo','players_number','avg_duration','price','geek_rating','avg_rating','game_year','game_description','category']