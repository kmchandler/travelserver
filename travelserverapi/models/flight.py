from django.db import models
from . import ItineraryItem

class Flight(ItineraryItem):
    itinerary_item = models.ForeignKey(ItineraryItem, related_name="flights", on_delete=models.CASCADE)
    departure_airport = models.CharField(max_length=100)
    departure_time = models.TimeField()
    arrival_airport = models.CharField(max_length=100)
    arrival_time = models.TimeField()
    layover = models.BooleanField()
