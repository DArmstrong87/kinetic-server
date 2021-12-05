from rest_framework import serializers
from kineticapi.models import Athlete
from django.contrib.auth import get_user_model
from kineticapi.serializers.event_serializer import EventSerializer

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'username')
        

class AthleteSerializer (serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Athlete
        fields = ('id',
                  'user',
                  'bio',
                  'sex',
                  'VO2_max',
                  'rhr',
                  'fluid_loss',
                  'sodium_loss',
                  'weight',
                  'height',
                  'user',
                  'age'
                  )
        depth = 1