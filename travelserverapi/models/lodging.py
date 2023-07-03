from django.db import models
from . import ItineraryItem
from . import Address

class Lodging(ItineraryItem):
    itinerary_item = models.ForeignKey(ItineraryItem, related_name="lodgings", on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=100)
    checkin_time = models.TimeField(null=True)
    checkout_time = models.TimeField(null=True)
