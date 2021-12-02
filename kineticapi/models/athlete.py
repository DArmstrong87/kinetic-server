from django.db import models
from django.contrib.auth.models import User


class Athlete(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=100)
    dob = models.DateField()
    sex = models.CharField(max_length=1)
    VO2_max = models.FloatField(null=True)
    rhr = models.IntegerField()
    fluid_loss = models.FloatField(null=True)
    sodium_loss = models.FloatField(null=True)
    weight = models.IntegerField()
    height = models.IntegerField()
    is_athlete = models.BooleanField(default=True)
