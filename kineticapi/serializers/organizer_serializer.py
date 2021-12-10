from rest_framework import serializers
from kineticapi.models import Organizer
from django.contrib.auth import get_user_model


class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username',)


class OrganizerSerializer (serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Organizer
        fields = ('organization', 'user')
        depth = 1
