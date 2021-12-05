"""View module for handling requests about game types"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from kineticapi.models import AthleteEvent
from kineticapi.models.athlete import Athlete
from kineticapi.serializers.athlete_event_serializer import AthleteEventSerializer


class AthleteEventView(ViewSet):
    """Kinetic Events"""

    def list(self, request):
        """Handle GET requests to get all events, ordered by nearest date. 
        Returns:
        Response -- JSON serialized list of events
        """
        
        athlete = Athlete.objects.get(user=request.auth.user)
        events = AthleteEvent.objects.filter(athlete=athlete)

        serializer = AthleteEventSerializer(
            events, many=True, context={'request': request})
        return Response(serializer.data)

