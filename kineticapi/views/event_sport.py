"""View module for handling requests about game types"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from kineticapi.models import Event, Sport, EventSport
from kineticapi.serializers import EventSerializer
from rest_framework import status

from kineticapi.serializers.event_serializer import EventSportSerializer


class EventSportView(ViewSet):
    """Kinetic EventSports"""

    def create(self, request):
        """Handles CREATE for a new event"""

        try:
            event=Event.objects.get(pk=request.data['eventId'])
            sport=Sport.objects.get(pk=request.data['sportId'])
            event_sport = EventSport.objects.create(
                event=event,
                sport=sport,
                distance=request.data['distance'],
                elev_gain=request.data['elevGain']
            )
            
            serializer = EventSportSerializer(
                event_sport, many=False, context={"request": request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
