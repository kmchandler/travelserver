from django.db import models
from .trip import Trip

class ItineraryItem(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    date = models.DateField()
    company_name = models.CharField(max_length=150)
    confirmation_number = models.CharField(max_length=100)
