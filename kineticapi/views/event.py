"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from kineticapi.models import Event
from kineticapi.serializers import EventSerializer


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
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single event
        Returns:
        Response -- JSON serialized event
        """
        try:
            event = Event.objects.get(pk=pk)
            serializer = EventSerializer(
                event, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
