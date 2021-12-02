from django.db import models


class Activity(models.Model):

    athlete = models.ForeignKey("Athlete", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    created_on = models.DateField()
