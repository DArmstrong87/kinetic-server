"""View module for handling requests about game types"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from kineticapi.models import Sport
from kineticapi.serializers import SportSerializer


class SportView(ViewSet):
    """Kinetic Sports"""

    def list(self, request):
        """Handle GET requests to get all sports
        Returns:
        Response -- JSON serialized list of sports
        """
        sports = Sport.objects.all()

        serializer = SportSerializer(
            sports, many=True, context={'request': request})
        return Response(serializer.data)