from rest_framework import serializers
from .models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['name','year','geek_rating','avg_rating','num_voters','rank' ]

