from django.db import models
from . import Itinerary
from . import Address

class Event(Itinerary):
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
    date = models.DateField()
    name = models.CharField(max_length=100)
    confirmation_number = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    address = models.ForeignKey(Address, on_delete=models.SET_NULL)
    phone_number = models.CharField(max_length=100)
