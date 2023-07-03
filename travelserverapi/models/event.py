from django.db import models
from . import ItineraryItem
from . import Address

class Event(ItineraryItem):
    itinerary_item = models.ForeignKey(ItineraryItem, related_name="events", on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField(null=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=100)
