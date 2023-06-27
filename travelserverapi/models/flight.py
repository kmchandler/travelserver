from django.db import models
from . import Itinerary

class Flight(Itinerary):
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
    date = models.DateField()
    confirmation_number = models.CharField(max_length=100)
    airline = models.CharField(max_length=100)
    departure_airport = models.CharField(max_length=100)
    departure_time = models.TimeField()
    arrival_airport = models.CharField(max_length=100)
    arrival_time = models.TimeField()
    layover = models.BooleanField()
