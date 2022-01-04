from django.db import models


class AthleteBadge(models.Model):

    athlete = models.ForeignKey("Athlete", on_delete=models.CASCADE)
    badge = models.ForeignKey("Badge", on_delete=models.CASCADE, related_name="athlete_badge")
    achieved_on = models.DateField()

    def __str__ (self): return f"{self.athlete} achieved {self.badge}"