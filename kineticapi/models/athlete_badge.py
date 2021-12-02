from django.db import models


class AthleteBadge(models.Model):

    athlete = models.ForeignKey("Athlete", on_delete=models.CASCADE)
    badge = models.ForeignKey("Badge", on_delete=models.CASCADE)
    achieved_on = models.DateField()

