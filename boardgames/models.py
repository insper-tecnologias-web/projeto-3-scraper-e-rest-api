from django.db import models


# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    geek_rating = models.FloatField()
    avg_rating = models.FloatField()
    num_voters = models.IntegerField()
    rank = models.IntegerField()
    # id = models.BigAutoField(primary_key=True)

    def __str__(self):
        string = self.name
        return string

