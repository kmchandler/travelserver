from django.db import models
from . import ItineraryItem
from . import Address

class RentalCar(ItineraryItem):
    itinerary_item = models.ForeignKey(ItineraryItem, related_name="rental cars", on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=100)
    pickup_time = models.TimeField()
    dropoff_time = models.TimeField()
