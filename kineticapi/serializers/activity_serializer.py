from rest_framework import serializers
from kineticapi.models import Activity
from kineticapi.models.activity_sport import ActivitySport
from kineticapi.serializers.organizer_serializer import OrganizerSerializer
from kineticapi.serializers.sport_serializer import SportSerializer


class ActivitySerializer (serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = ('id',
                  'name',
                  'created_on'
                  )
        depth = 1

class ActivitySportSerializer (serializers.ModelSerializer):
    sport = SportSerializer()
    activity = ActivitySerializer()

    class Meta:
        model = ActivitySport
        fields = ('id', 'activity', 'sport', 'distance', 'elev_gain')

