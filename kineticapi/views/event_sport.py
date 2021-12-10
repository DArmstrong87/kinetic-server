"""View module for handling requests about game types"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from kineticapi.models import Event, Sport, EventSport, event_sport
from kineticapi.serializers import EventSerializer
from rest_framework import status

from kineticapi.serializers.event_serializer import EventSportSerializer


class EventSportView(ViewSet):
    """Kinetic EventSports"""

    def create(self, request):
        """Handles CREATE for a new event"""

        try:
            event = Event.objects.get(pk=request.data['eventId'])
            sport = Sport.objects.get(pk=request.data['sportId'])
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

    def update(self, request, pk=None):
        """Handle updating event sports as events get updated"""
        
        event_sport = EventSport.objects.get(pk=pk)
        event_sport.distance = request.data['distance']
        event_sport.elevGain = request.data['elevGain']
        event_sport.save()
        
        serializer = EventSportSerializer(
                event_sport, many=False, context={"request": request})
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk=None):
        event_sport = EventSport.objects.get(pk=pk)
        event_sport.delete()
        return Response ("Event sport deleted", status=status.HTTP_204_NO_CONTENT)