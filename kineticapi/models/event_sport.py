from django.db import models


class EventSport(models.Model):

    event = models.ForeignKey("Event", on_delete=models.CASCADE)
    sport = models.ForeignKey("Sport", on_delete=models.CASCADE)
    distance = models.FloatField()
    elev_gain = models.FloatField()
    