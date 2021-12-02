from django.db import models


class ActivitySport(models.Model):

    activity = models.ForeignKey("Activity", on_delete=models.CASCADE)
    sport = models.ForeignKey("Sport", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    created_on = models.DateField()
    distance = models.FloatField()
    elev_gain = models.FloatField()
