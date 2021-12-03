"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from kineticapi.models import Event
from kineticapi.serializers import EventSerializer


class EventView(ViewSet):
    """Level up game types"""

    def list(self, request):
        """Handle GET requests to get all game types
        Returns:
        Response -- JSON serialized list of game types
        """
        events = Event.objects.all()

        serializer = EventSerializer(
            events, many=True, context={'request': request})
        return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     """Handle GET requests for single game type
    #     Returns:
    #     Response -- JSON serialized game type
    #     """
    #     try:
    #         game_type = GameType.objects.get(pk=pk)
    #         serializer = GameTypeSerializer(
    #             game_type, context={'request': request})
    #         return Response(serializer.data)
    #     except Exception as ex:
    #         return HttpResponseServerError(ex)
