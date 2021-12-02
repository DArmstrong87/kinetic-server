from django.db import models


class Event(models.Model):

    organizer = models.ForeignKey("Organizer", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateTimeField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=14)
    max_participants = models.IntegerField()
    course_url = models.URLField()
    event_logo = models.URLField()
    
    #TODO Add a custom property for total distance.