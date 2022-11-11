from django.db import models
from django.contrib.auth.models import User


class EventGamer(models.Model):

    gamer = models.ForeignKey("Gamer", null=True, blank=True, on_delete=models.CASCADE)
    event = models.ForeignKey("Event", null=True, blank=True, on_delete=models.CASCADE)
