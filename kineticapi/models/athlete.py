from django.db import models
from django.contrib.auth.models import User
from datetime import date


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
    
    def __str__ (self): return f"{self.user.first_name} {self.user.last_name}"

    @property
    def age(self):
        """Find the athlete's age"""
        d = date.today()
        age = (d.year - self.dob.year) - \
            int((d.month, d.day) < (self.dob.month, self.dob.day))

        return age

    # TODO Custom properties for total distances based on sports participated in.
