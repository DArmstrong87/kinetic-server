from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from kineticapi.models import AthleteBadge, Athlete, Badge
from rest_framework import status
from kineticapi.serializers import AthleteBadgeSerializer
from datetime import datetime
from datetime import date


class AthleteBadgeView(ViewSet):
    """Kinetic Athlete Badges aka Achievements"""

    def list(self, request):
        """List athlete badges"""

        athlete = Athlete.objects.get(user=request.auth.user)
        athlete_badges = AthleteBadge.objects.filter(athlete=athlete).order_by('achieved_on')
        
        limit = self.request.query_params.get('limit', None)
        
        if limit is not None:
            athlete_badges = AthleteBadge.objects.filter(athlete=athlete).order_by('achieved_on')[:10]

        serializer = AthleteBadgeSerializer(
            athlete_badges, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Create athlete badge"""

        athlete = Athlete.objects.get(user=request.auth.user)
        badge = Badge.objects.get(pk=request.data['badgeId'])

        try:
            athlete_badge = AthleteBadge.objects.create(
                athlete=athlete,
                badge=badge,
                achieved_on=date.today()
            )
            serialier = AthleteBadgeSerializer(
                athlete_badge, many=False,  context={'request': request})
            return Response(serialier.data, status=status.HTTP_201_CREATED)

        except Exception as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
