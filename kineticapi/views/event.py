"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from kineticapi.models import Event, Athlete, AthleteEvent, Organizer
from kineticapi.serializers import EventSerializer
from rest_framework.decorators import action
from rest_framework import status


class EventView(ViewSet):
    """Kinetic Events"""

    def list(self, request):
        """Handle GET requests to get all events, ordered by nearest date. 
        Returns:
        Response -- JSON serialized list of events
        """
        
        events = Event.objects.all().order_by('date')

        serializer = EventSerializer(
            events, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single event
        Returns:
        Response -- JSON serialized event
        """
        try:
            event = Event.objects.get(pk=pk)
            serializer = EventSerializer(
                event, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return HttpResponseServerError(ex)

    @action(methods=['post', 'delete'], detail=True, url_path="signup")
    def signup(self, request, pk):
        """Sign up for event"""
        athlete = Athlete.objects.get(user=request.auth.user)
        event = Event.objects.get(pk=pk)

        if request.method == "POST":
            try:
                athlete_event = AthleteEvent.objects.get(
                    athlete=athlete, event=event)
                return Response({f"You have already signed up for {event.name}"})
            except:
                athlete_event = AthleteEvent.objects.create(
                    athlete=athlete,
                    event=event
                )
                return Response({f"You have signed up for {event.name}!"}, status=status.HTTP_201_CREATED)
        elif request.method == "DELETE":
            try:
                athlete_event = AthleteEvent.objects.get(
                    athlete=athlete, event=event)
                athlete_event.delete()
                return Response({f"You have left {event.name}."}, status=status.HTTP_204_NO_CONTENT)
            except:
                return Response({"This event was not found."}, status=status.HTTP_404_NOT_FOUND)

class OrganizerEventView(ViewSet):
    """Kinetic Events"""

    def list(self, request):
        """Handle GET requests to get all events, ordered by nearest date. 
        Returns:
        Response -- JSON serialized list of events
        """

        organizer = Organizer.objects.get(user=request.auth.user)
        
        events = Event.objects.all().order_by('date').filter(organizer=organizer)

        serializer = EventSerializer(
            events, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)