from django.db import models


class ActivitySport(models.Model):

    activity = models.ForeignKey("Activity", on_delete=models.CASCADE, related_name="activity_sports")
    sport = models.ForeignKey("Sport", on_delete=models.CASCADE)
    distance = models.FloatField()
    elev_gain = models.FloatField()

    def __str__ (self): return f"{self.sport.name}"