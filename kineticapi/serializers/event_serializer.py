from rest_framework import serializers
from kineticapi.models import Event, EventSport, Sport
from kineticapi.serializers.sport_serializer import SportSerializer



class EventSportSerializer (serializers.ModelSerializer):

    class Meta:
        model = EventSport
        fields = ('id', 'sport', 'distance', 'elev_gain')
        depth = 1


class EventSerializer (serializers.ModelSerializer):
    # event_sports = EventSportSerializer()

    class Meta:
        model = Event
        fields = ('id',
                  'name',
                  'description',
                  'date',
                  'city',
                  'state',
                  'max_participants',
                  'course_url',
                  'event_logo'
                  )
        depth=1
