from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.db.models.aggregates import Sum
from kineticapi.models.activity import Activity


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

    def __str__(self): return f"{self.user.first_name} {self.user.last_name}"

    @property
    def age(self):
        """Find the athlete's age"""
        d = date.today()
        age = (d.year - self.dob.year) - \
            int((d.month, d.day) < (self.dob.month, self.dob.day))

        return age

    # TODO Custom properties for total distances based on sports participated in.
    @property
    def distanceYTD(self):
        """Sum of this year's total distance"""
        d = date.today()
        total_distance = 0
        act = Activity.objects.annotate(dist=Sum("activity_sports__distance")).filter(created_on__year=d.year, athlete=self)
        for a in act:
            total_distance += a.dist
        return total_distance
    
    @property
    def elevGainYTD(self):
        """Sum of this year's total elevation gain"""
        d = date.today()
        gain = 0
        act = Activity.objects.annotate(gain=Sum("activity_sports__elev_gain")).filter(created_on__year=d.year, athlete=self)
        for a in act:
            gain += a.gain
        return gain
