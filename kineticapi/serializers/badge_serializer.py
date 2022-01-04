from rest_framework import serializers
from kineticapi.models import Badge


class BadgeSerializer (serializers.ModelSerializer):

    class Meta:
        model = Badge
        fields = ('id', 'name', 'description', 'complete_url', 'incomplete_url')
