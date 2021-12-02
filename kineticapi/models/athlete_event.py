from django.db import models


class AthleteEvent(models.Model):

    event = models.ForeignKey("Event", on_delete=models.CASCADE)
    athlete = models.ForeignKey("Athlete", on_delete=models.CASCADE)

