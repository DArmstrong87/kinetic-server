from django.db import models


class Badge(models.Model):

    name = models.CharField(max_length=50)
    incomplete = models.URLField()
    complete = models.URLField()
