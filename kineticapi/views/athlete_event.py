"""View module for handling requests about game types"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from kineticapi.models import AthleteEvent, Athlete, Event
from kineticapi.serializers.athlete_event_serializer import AthleteEventSerializer


class AthleteEventView(ViewSet):
    """Kinetic Events"""

    def list(self, request):
        """Handle GET requests to get all events, ordered by nearest date. 
        Returns:
        Response -- JSON serialized list of events
        """
        
        athlete = Athlete.objects.get(user=request.auth.user)
        events = AthleteEvent.objects.filter(athlete=athlete).order_by('-date')

        serializer = AthleteEventSerializer(
            events, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk):
        """Get single athlete event"""
        athlete = Athlete.objects.get(user=request.auth.user)
        event=Event.objects.get(pk=pk)
        athlete_event = AthleteEvent.objects.get(athlete=athlete, event=event)
        
        serializer = AthleteEventSerializer(
            athlete_event, context={'request': request})
        return Response(serializer.data)