from rest_framework import serializers
from kineticapi.models import Activity
from kineticapi.models.activity_sport import ActivitySport
from kineticapi.serializers.sport_serializer import SportSerializer


class ActivitySportSerializer (serializers.ModelSerializer):
    sport = SportSerializer()

    class Meta:
        model = ActivitySport
        fields = ('id', 'activity', 'sport', 'distance', 'elev_gain')


class ActivitySerializer (serializers.ModelSerializer):
    activity_sports = ActivitySportSerializer(many=True)

    class Meta:
        model = Activity
        fields = ('id',
                  'name',
                  'created_on',
                  'activity_sports',
                  'total_distance',
                  'total_elev_gain'
                  )
        depth = 1

