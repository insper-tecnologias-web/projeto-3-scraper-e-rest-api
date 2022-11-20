from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=100)
    rank = models.IntegerField()
    photo = models.CharField(max_length=500)
    players_number = models.IntegerField()
    avg_duration = models.IntegerChoices()
    price = models.FloatField(default="Undefined")
    geek_rating = models.FloatField()
    avg_rating = models.FloatField()
    game_year = models.IntegerField()
    game_description = models.CharField(max_length=1000)
    category = models.CharField(max_length=50)
    # id = models.BigAutoField(primary_key=True)
    
    def __str__ (self):
        string = self.name
        return string