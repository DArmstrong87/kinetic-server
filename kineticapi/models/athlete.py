from django.db import models
from django.contrib.auth.models import User

class Athlete(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
