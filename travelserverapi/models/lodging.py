from django.db import models
from . import Itinerary
from . import Address

class Lodging(Itinerary):
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
    date = models.DateField()
    name = models.CharField(max_length=100)
    confirmation_number = models.CharField(max_length=100)
    company= models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL)
    phone_number = models.CharField(max_length=100)
    checkin_time = models.TimeField()
    checkout_time = models.TimeField()
