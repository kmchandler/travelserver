from django.db import models
from . import ItineraryItem
from . import Address

class Train(ItineraryItem):
    itinerary_item = models.ForeignKey(ItineraryItem, related_name="trains", on_delete=models.CASCADE)
    departure_station = models.CharField(max_length=100)
    departure_station_address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    departure_time = models.TimeField()
    arrival_station = models.CharField(max_length=100)
    arrival_station_address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    arrival_time = models.TimeField()
