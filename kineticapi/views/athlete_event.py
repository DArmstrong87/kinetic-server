"""View module for handling requests about game types"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from kineticapi.models import AthleteEvent, Athlete, Event
from kineticapi.serializers.athlete_event_serializer import AthleteEventSerializer
from rest_framework import status
from datetime import datetime


class AthleteEventView(ViewSet):
    """Kinetic Events"""

    def list(self, request):
        """Handle GET requests to get all events, ordered by nearest date. 
        Returns:
        Response -- JSON serialized list of events
        """

        athlete = Athlete.objects.get(user=request.auth.user)
        past = self.request.query_params.get('past', None)

        if past is not None:
            events = AthleteEvent.objects.filter(
                athlete=athlete, event__date__lt=datetime.now()).order_by('event__date')
        else:
            events = AthleteEvent.objects.filter(
                athlete=athlete, event__date__gte=datetime.now()).order_by('event__date')

        serializer = AthleteEventSerializer(
            events, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk):
        """Get single athlete event"""
        athlete = Athlete.objects.get(user=request.auth.user)
        event = Event.objects.get(pk=pk)
        athlete_event = AthleteEvent.objects.get(athlete=athlete, event=event)

        serializer = AthleteEventSerializer(
            athlete_event, context={'request': request})
        return Response(serializer.data)
    
    def partial_update(self, request, pk):
        """Update Athlete Event"""
        athlete = Athlete.objects.get(user=request.auth.user)
        athlete_event = AthleteEvent.objects.get(athlete=athlete, pk=pk)
        athlete_event.completed = request.data['completed']
        athlete_event.save()
        
        return Response("athlete event updated", status=status.HTTP_204_NO_CONTENT)
