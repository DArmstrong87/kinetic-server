"""View module for handling requests about game types"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from kineticapi.models import Activity, Sport, ActivitySport, ActivitySport
from rest_framework import status
from kineticapi.serializers import ActivitySportSerializer


class ActivitySportView(ViewSet):
    """Kinetic ActivitySports"""

    def create(self, request):
        """Handles CREATE for a new activity"""

        try:
            activity = Activity.objects.get(pk=request.data['activityId'])
            sport = Sport.objects.get(pk=request.data['sportId'])
            activity_sport = ActivitySport.objects.create(
                activity=activity,
                sport=sport,
                distance=request.data['distance'],
                elev_gain=request.data['elevGain']
            )

            serializer = ActivitySportSerializer(
                activity_sport, many=False, context={"request": request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        """Handle updating activity sports as activities get updated"""
        
        activity_sport = ActivitySport.objects.get(pk=pk)
        sport=Sport.objects.get(pk=request.data['sportId'])
        activity_sport.sport = sport
        activity_sport.distance = request.data['distance']
        activity_sport.elev_gain = request.data['elevGain']
        activity_sport.save()
        
        serializer = ActivitySportSerializer(
                activity_sport, many=False, context={"request": request})
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk=None):
        activity_sport = ActivitySport.objects.get(pk=pk)
        activity_sport.delete()
        return Response ("Activity sport deleted", status=status.HTTP_204_NO_CONTENT)