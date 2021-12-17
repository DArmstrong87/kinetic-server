from django.db import models
from kineticapi.models.activity_sport import ActivitySport



class Activity(models.Model):

    athlete = models.ForeignKey("Athlete", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    created_on = models.DateField()

    def __str__(self): return self.name

    @property
    def total_distance(self):
        """Add total distance"""
        total_distance = 0
        try:
            activity_sports = ActivitySport.objects.filter(activity=self)
            for actSp in activity_sports:
                total_distance += actSp.distance
            return total_distance
        except:
            return 0

    @property
    def total_elev_gain(self):
        """Add total elevation gain"""
        total_elev = 0
        try:
            activity_sports = ActivitySport.objects.filter(activity=self)
            for actSp in activity_sports:
                total_elev += actSp.elev_gain
            return total_elev
        except:
            return 0
