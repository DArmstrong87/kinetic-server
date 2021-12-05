from django.db import models
import json
from kineticapi.models.event_sport import EventSport


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
    event_sport = models.ForeignKey("EventSport", on_delete=models.CASCADE, related_name="event_sports")
    
    @property
    def total_distance(self):
        """Add total distance"""
        event_sports = EventSport.objects.filter(event=self)
        total_distance = 0
        for es in event_sports:
            total_distance += es.distance
        return total_distance
    
    @property
    def total_elev_gain(self):
        """Add total elevation gain"""
        event_sports = EventSport.objects.filter(event=self)
        total_elev = 0
        for es in event_sports:
            total_elev += es.elev_gain
        return total_elev