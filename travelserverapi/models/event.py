from django.db import models
from . import ItineraryItem
from . import Address

class Event(ItineraryItem):
    itinerary = models.ForeignKey(ItineraryItem, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    address = models.ForeignKey(Address, on_delete=models.SET_NULL)
    phone_number = models.CharField(max_length=100)
