from django.contrib import admin
from rest_framework import routers
from django.conf.urls import include
from django.urls import path
from kineticapi.views import register_user, login_user, EventView
from kineticapi.views.athlete_event import AthleteEventView
from kineticapi.views.event import OrganizerEventView
from kineticapi.views.event_sport import EventSportView
from kineticapi.views.profile import AthleteView
from kineticapi.views.sport import SportView
"""kinetic URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
"""
router = routers.DefaultRouter(trailing_slash=False)
router.register(r'events', EventView, 'event')
router.register(r'organizerevents', OrganizerEventView, 'organizerevent')
router.register(r'sports', SportView, 'sport')
router.register(r'athleteevents', AthleteEventView, 'athleteevent')
router.register(r'athletes', AthleteView, 'athlete')
router.register(r'eventsports', EventSportView, 'eventsport')

urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls',
                             namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
