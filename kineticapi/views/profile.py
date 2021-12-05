"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from kineticapi.models import Athlete
from rest_framework import status
from kineticapi.serializers import AthleteSerializer


class AthleteView(ViewSet):
    """Kinetic athlete profile"""

    def list(self, request):
        """Handle GET requests for single event
        Returns:
        Response -- JSON serialized event
        """
        try:
            athlete = Athlete.objects.get(user=request.auth.user)
            serializer = AthleteSerializer(
                athlete, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return HttpResponseServerError(ex)
