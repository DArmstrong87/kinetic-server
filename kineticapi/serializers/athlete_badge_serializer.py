from rest_framework import serializers
from kineticapi.models import AthleteBadge
from .badge_serializer import BadgeSerializer


class AthleteBadgeSerializer (serializers.ModelSerializer):
    badge = BadgeSerializer()

    class Meta:
        model = AthleteBadge
        fields = ('id', 'badge', 'achieved_on')
