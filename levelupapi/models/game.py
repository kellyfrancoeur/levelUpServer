from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):

    game_type = models.ForeignKey("GameType", null=True, blank=True, on_delete=models.CASCADE, related_name='game_type')
    title = models.CharField(max_length=50)
    maker = models.CharField(max_length=50)
    gamer = models.ForeignKey("Gamer", null=True, blank=True, on_delete=models.CASCADE, related_name='gamer' )
    number_of_players = models.IntegerField(null=True, blank=True)
    skill_level = models.IntegerField(null=True, blank=True)
