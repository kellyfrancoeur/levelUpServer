"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Game
from levelupapi.models import Gamer
from levelupapi.models import GameType

class GameView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        game = Game.objects.get(pk=pk)
        serializer = GameSerializer(game)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

    def create(self, request):
        
        new_game = Game()
        new_game.title = request.data["title"]
        new_game.maker = request.data["maker"]
        new_game.number_of_players = request.data["number_of_players"]
        new_game.skill_level = request.data["skill_level"]
        new_game.gamer = Gamer.objects.get(user=request.auth.user)
        new_game.game_type = GameType.objects.get(pk=request.data["game_type"])

        
        serializer = GameSerializer(new_game)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        """Handle PUT requests for a game

        Returns:
        Response -- Empty body with 204 status code
        """
        game_type = GameType.objects.get(pk=request.data["game_type"])

        game = Game.objects.get(pk=pk)
        game.title = request.data["title"]
        game.maker = request.data["maker"]
        game.number_of_players = request.data["number_of_players"]
        game.skill_level = request.data["skill_level"]
        game.game_type = game_type
        game.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

class GamerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gamer
        fields = ('id',)

class GameTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameType
        fields = ('id',)

class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    gamer = GamerSerializer(many=False)
    game_type = GameTypeSerializer (many=False)
    class Meta:
        model = Game
        fields = ('id', 'game_type', 'title', 'maker', 'gamer', 'number_of_players', 'skill_level',)
        depth = 1
