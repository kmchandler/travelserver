from django.db import models
from .trip import Trip

class Itinerary(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
