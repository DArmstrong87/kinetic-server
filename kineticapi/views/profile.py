"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from kineticapi.models import Athlete
from rest_framework import status
from kineticapi.serializers import AthleteSerializer
from django.contrib.auth.models import User


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

    def update(self, request, pk=None):
        """Handle updating of athlete"""

        try:
            athlete = Athlete.objects.get(pk=request.data['id'])
            athlete.bio = request.data["bio"],
            athlete.VO2_max = request.data["VO2max"],
            athlete.rhr = request.data["rhr"],
            athlete.fluid_loss = request.data["fluidLoss"],
            athlete.sodium_loss = request.data["sodiumLoss"],
            athlete.weight = request.data["weight"],
            athlete.dob = athlete.dob,
            athlete.height = athlete.height,
            athlete.is_athlete = athlete.is_athlete
            athlete.save()

            # user = User.objects.get(user=athlete.user)
            # user.first_name=request.data['firstName']
            # user.last_name=request.data['lastName']
            # user.save()
            return Response({"message": "User updated!"}, status=status.HTTP_204_NO_CONTENT)

        except Exception as ex:
            return Response(ex.args[0], status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def partial_update(self, request, pk=None):
        """Handle partially updating an athlete property"""

        athlete = Athlete.objects.get(user=request.auth.user)
        if request.data['VO2max']:
            athlete.VO2_max = request.data['VO2max']
        elif request.data['fluidLoss']:
            athlete.fluid_loss = request.data['fluidLoss']
        elif request.data['sodiumLoss']:
            athlete.sodium_loss = request.data['sodiumLoss']
        athlete.save()
        return Response({"message": f"Property updated!"}, status=status.HTTP_204_NO_CONTENT)
