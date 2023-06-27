from django.db import models
from . import Itinerary
from . import Address

class RentalCar(Itinerary):
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
    date = models.DateField()
    confirmation_number = models.CharField(max_length=100)
    company= models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL)
    phone_number = models.CharField(max_length=100)
    pickup_time = models.TimeField()
    dropoff_time = models.TimeField()
