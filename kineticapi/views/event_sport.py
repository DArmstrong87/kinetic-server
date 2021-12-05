"""View module for handling requests about game types"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from kineticapi.models import EventSport
from kineticapi.serializers.event_serializer import EventSportSerializer


class EventSportView(ViewSet):
    """Level up game types"""

    def list(self, request):
        """Handle GET requests to get all game types
        Returns:
        Response -- JSON serialized list of game types
        """
        event_sport = EventSport.objects.all()
        event_id = request.query_params.get('event', None)
        if event_id:
            event_sport = event_sport.filter(event_id=event_id)

        serializer = EventSportSerializer(
            event_sport, many=True, context={'request': request})
        return Response(serializer.data)
