"""View module for handling requests about game types"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from kineticapi.models import EventSport
from kineticapi.serializers import EventSportSerializer


class EventSportView(ViewSet):
    """Level up game types"""

    def list(self, request):
        """Handle GET requests to get all game types
        Returns:
        Response -- JSON serialized list of game types
        """
        event_sport = EventSport.objects.all()

        serializer = EventSportSerializer(
            event_sport, many=True, context={'request': request})
        return Response(serializer.data)