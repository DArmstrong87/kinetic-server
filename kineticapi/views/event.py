"""View module for handling requests about game types"""
from django.db.models.aggregates import Sum
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from kineticapi.models import Event, Athlete, AthleteEvent, Organizer, EventSport
from kineticapi.serializers import EventSerializer
from rest_framework.decorators import action
from rest_framework import status
from django.db.models import Q
from datetime import datetime


class EventView(ViewSet):
    """Kinetic Events"""

    def list(self, request):
        """Handle GET requests to get all events, ordered by nearest date.
        Returns:
        Response -- JSON serialized list of events
        """

        events = Event.objects.all().order_by('date')

        search_term = self.request.query_params.get('q', None)
        distance = self.request.query_params.get('dist', None)
        state = self.request.query_params.get('state', None)
        month = self.request.query_params.get('month', None)
        past = self.request.query_params.get('past', None)

        if search_term is not None:
            events = Event.objects.filter(
                Q(name__icontains=search_term) |
                Q(description__icontains=search_term) |
                Q(city__icontains=search_term) |
                Q(state__icontains=search_term)
            )

        if distance is not None:
            events = Event.objects.annotate(
                tdist=Sum("event_sports__distance")).filter(tdist__gte=distance)

        if state is not None:
            events = Event.objects.filter(state=state)

        if month is not None:
            events = Event.objects.filter(date__month=month)
        
        if past is not None:
            events = Event.objects.filter(date__lt=datetime.now())
        else:
            events = Event.objects.filter(date__gte=datetime.now())


        serializer = EventSerializer(
            events, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single event
        Returns:
        Response -- JSON serialized event
        """
        try:
            event = Event.objects.get(pk=pk)
            serializer = EventSerializer(
                event, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def create(self, request):
        """Handles CREATE for a new event"""

        try:
            organizer = Organizer.objects.get(user=request.auth.user)
            event = Event.objects.create(
                name=request.data['name'],
                description=request.data['description'],
                date=request.data['date'],
                city=request.data['city'],
                state=request.data['state'],
                max_participants=request.data['maxParticipants'],
                course_url=request.data['courseUrl'],
                event_logo=request.data['eventLogo'],
                organizer=organizer
            )

            serializer = EventSerializer(
                event, many=False, context={"request": request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk):
        """Handles CREATE for a new event"""

        organizer = Organizer.objects.get(user=request.auth.user)
        try:
            event = Event.objects.get(pk=pk, organizer=organizer)
            event.name = request.data['name']
            event.description = request.data['description']
            event.date = request.data['date']
            event.city = request.data['city']
            event.state = request.data['state']
            event.max_participants = request.data['maxParticipants']
            event.course_url = request.data['courseUrl']
            event.event_logo = request.data['eventLogo']
            event.save()

            serializer = EventSerializer(
                event, many=False, context={"request": request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # else:
        #     return Response("You are not authorized to edit this event.", status=status.HTTP_401_UNAUTHORIZED)

    def destroy(self, request, pk=None):
        try:
            event = Event.objects.get(pk=pk)
            event.delete()

            return Response({"event deleted"}, status=status.HTTP_204_NO_CONTENT)

        except Event.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    @action(methods=['post', 'delete'], detail=True, url_path="signup")
    def signup(self, request, pk):
        """Sign up for event"""
        athlete = Athlete.objects.get(user=request.auth.user)
        event = Event.objects.get(pk=pk)

        if request.method == "POST":
            try:
                athlete_event = AthleteEvent.objects.get(
                    athlete=athlete, event=event)
                return Response({f"You have already signed up for {event.name}"})
            except:
                athlete_event = AthleteEvent.objects.create(
                    athlete=athlete,
                    event=event
                )
                return Response({f"You have signed up for {event.name}!"}, status=status.HTTP_201_CREATED)
        elif request.method == "DELETE":
            try:
                athlete_event = AthleteEvent.objects.get(
                    athlete=athlete, event=event)
                athlete_event.delete()
                return Response({f"You have left {event.name}."}, status=status.HTTP_204_NO_CONTENT)
            except:
                return Response({"This event was not found."}, status=status.HTTP_404_NOT_FOUND)


class OrganizerEventView(ViewSet):
    """Kinetic Events"""

    def list(self, request):
        """Handle GET requests to get all events, ordered by nearest date. 
        Returns:
        Response -- JSON serialized list of events
        """

        organizer = Organizer.objects.get(user=request.auth.user)
        past = self.request.query_params.get('past', None)
        
        if past is not None:
            events = Event.objects.filter(organizer=organizer, date__lt=datetime.now()).order_by('date')
        else:
            events = Event.objects.filter(organizer=organizer, date__gte=datetime.now()).order_by('date')

        serializer = EventSerializer(
            events, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
