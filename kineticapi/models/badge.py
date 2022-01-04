from django.db import models


class Badge(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    incomplete_url = models.URLField()
    complete_url = models.URLField()

    def __str__ (self): return self.name