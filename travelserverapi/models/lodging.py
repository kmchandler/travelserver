from django.db import models
from . import ItineraryItem
from . import Address

class Lodging(ItineraryItem):
    itinerary = models.ForeignKey(ItineraryItem, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL)
    phone_number = models.CharField(max_length=100)
    checkin_time = models.TimeField()
    checkout_time = models.TimeField()
