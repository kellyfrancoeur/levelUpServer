"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Event
from levelupapi.models import Game
from levelupapi.models import Gamer


class EventView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
        Response -- JSON serialized game instance
    """
        game = Game.objects.get(pk=request.data["game"])
        organizer = Gamer.objects.get(user=request.auth.user)

        event = Event.objects.create(
            game=game,
            description=request.data["description"],
            date=request.data["date"],
            time=request.data["time"],
            organizer=organizer
        )
        serializer = EventSerializer(event)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        """Handle PUT requests for a game

        Returns:
        Response -- Empty body with 204 status code
        """
        game = Game.objects.get(pk=request.data["game"])
        organizer = Gamer.objects.get(pk=request.data["organizer"])

        event = Event.objects.get(pk=pk)
        event.description = request.data["description"]
        event.date = request.data["date"]
        event.time = request.data["time"]
        event.organizer = organizer
        event.game = game
        event.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Event
        fields = ('id', 'game', 'description', 'date', 'time', 'organizer', 'attendees',)
