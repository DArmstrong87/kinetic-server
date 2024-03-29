"""View module for handling requests about game types"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from kineticapi.models import Badge, AthleteBadge, Athlete
from rest_framework import status
from django.db.models import Q
from kineticapi.serializers.badge_serializer import BadgeSerializer


class BadgeView(ViewSet):
    """Kinetic Badges"""

    def list(self, request):
        """Handle GET requests to get badges that have not yet been achieved
        Returns:
        Response -- JSON serialized list of badges
        """
        athlete = Athlete.objects.get(user=request.auth.user)

        achievements = [AthleteBadge.objects.filter(
            athlete=athlete).values('badge')]

        badges = Badge.objects.filter(~Q(pk__in=achievements))

        serializer = BadgeSerializer(
            badges, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Creates new badges"""

        try:
            badge = Badge.objects.create(
                name=request.data['name'],
                description=request.data['description'],
                complete_url=request.data['complete_url'],
                incomplete_url=request.data['incomplete_url']
            )

            serializer = BadgeSerializer(
                badge, many=False, context={"request": request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
