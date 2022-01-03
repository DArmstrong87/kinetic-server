"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from kineticapi.models import Event, Athlete, Activity
from rest_framework import status

from kineticapi.serializers.activity_serializer import ActivitySerializer


class ActivityView(ViewSet):
    """Kinetic Events"""

    def list(self, request):
        """Handle GET requests to get all events, ordered by nearest date.
        Returns:
        Response -- JSON serialized list of events
        """

        athlete = Athlete.objects.get(user=request.auth.user)
        activities = Activity.objects.filter(
            athlete=athlete).order_by('created_on')

        serializer = ActivitySerializer(
            activities, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single event
        Returns:
        Response -- JSON serialized event
        """
        try:
            activity = Activity.objects.get(pk=pk)
            serializer = ActivitySerializer(
                activity, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def create(self, request):
        """Handles CREATE for a new event"""

        try:
            athlete = Athlete.objects.get(user=request.auth.user)

            activity = Activity.objects.create(
                athlete=athlete,
                name=request.data['name'],
                created_on=request.data['createdOn']
            )

            serializer = ActivitySerializer(
                activity, many=False, context={"request": request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk):
        """Handles CREATE for a new event"""

        # athlete = Athlete.objects.get(user=request.auth.user)
        try:
            activity = Activity.objects.get(pk=pk)
            activity.name = request.data['name']
            activity.created_on = request.data['createdOn']
            activity.save()

            serializer = ActivitySerializer(
                activity, many=False, context={"request": request})
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

        except Exception as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # else:
        #     return Response("You are not authorized to edit this event.", status=status.HTTP_401_UNAUTHORIZED)

    def destroy(self, request, pk=None):
        try:
            activity = Activity.objects.get(pk=pk)
            activity.delete()

            return Response({"activity deleted"}, status=status.HTTP_204_NO_CONTENT)

        except Event.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
