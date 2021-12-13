from django.contrib import admin
from kineticapi.models import Sport, ActivitySport, Activity, Athlete, AthleteBadge, AthleteEvent, Badge, Event, EventSport, Organizer


# Register your models here.
admin.site.register(ActivitySport)
admin.site.register(Activity)
admin.site.register(AthleteBadge)
admin.site.register(AthleteEvent)
admin.site.register(Athlete)
admin.site.register(Badge)
admin.site.register(EventSport)
admin.site.register(Event)
admin.site.register(Organizer)
admin.site.register(Sport)