from django.db import models
from kineticapi.models.athlete_event import AthleteEvent
from kineticapi.models.event_sport import EventSport
from datetime import datetime


class Event(models.Model):

    organizer = models.ForeignKey("Organizer", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateTimeField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=14)
    max_participants = models.IntegerField()
    course_url = models.URLField()
    event_logo = models.URLField()

    @property
    def total_distance(self):
        """Add total distance"""
        total_distance = 0
        try:
            event_sports = EventSport.objects.filter(event=self)
            for es in event_sports:
                total_distance += es.distance
            return total_distance
        except:
            return total_distance

    @property
    def total_elev_gain(self):
        """Add total elevation gain"""
        try:
            event_sports = EventSport.objects.filter(event=self)
            total_elev = 0
            for es in event_sports:
                total_elev += es.elev_gain
            return total_elev
        except:
            return 0

    @property
    def spots_remaining(self):
        """Calculate spots remaining for event registration"""
        remaining = self.max_participants
        try:
            remaining -= AthleteEvent.objects.filter(event=self).count()
            return remaining
        except:
            return remaining

    @property
    def days_until(self):
        """Calculate days until the race"""
        today = datetime.now().timestamp()
        racetime = self.date.timestamp()
        daysUntil = round((racetime - today)/(3600*24))
        return daysUntil
