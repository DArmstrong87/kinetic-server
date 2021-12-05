from rest_framework import serializers
from kineticapi.models import Event, EventSport
from kineticapi.serializers.event_serializer import EventSerializer


class AthleteEventSerializer (serializers.ModelSerializer):
    event = EventSerializer()

    class Meta:
        model = Event
        fields = ('event',)
        depth = 1
