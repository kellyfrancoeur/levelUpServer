from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):

    game = models.ForeignKey("Game", null=True, blank=True, on_delete=models.CASCADE, related_name="game")
    description = models.CharField(max_length=50)
    date = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)
    time = models.TimeField()
    organizer = models.ForeignKey("Gamer", null=True, blank=True, on_delete=models.CASCADE, related_name="organizer")
    attendees = models.ManyToManyField("Gamer")
