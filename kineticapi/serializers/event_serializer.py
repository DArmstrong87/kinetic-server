from rest_framework import serializers
from kineticapi.models import Event, EventSport
from kineticapi.serializers.organizer_serializer import OrganizerSerializer
from kineticapi.serializers.sport_serializer import SportSerializer


class EventSportSerializer (serializers.ModelSerializer):
    sport = SportSerializer()

    class Meta:
        model = EventSport
        fields = ('id', 'event', 'sport', 'distance', 'elev_gain')


class EventSerializer (serializers.ModelSerializer):
    event_sports = EventSportSerializer(many=True)
    organizer = OrganizerSerializer()

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
                  'event_logo',
                  'event_sports',
                  'total_distance',
                  'total_elev_gain',
                  'spots_remaining',
                  'days_until',
                  'organizer'
                  )
        depth = 1
