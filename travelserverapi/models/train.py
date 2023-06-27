from django.db import models
from . import Itinerary
from . import Address

class Train(Itinerary):
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
    date = models.DateField()
    confirmation_number = models.CharField(max_length=100)
    airline = models.CharField(max_length=100)
    trainline_name = models.CharField(max_length=100)
    departure_station = models.CharField(max_length=100)
    departure_station_address = models.ForeignKey(Address, on_delete=models.SET_NULL)
    departure_time = models.TimeField()
    arrival_station = models.CharField(max_length=100)
    arrival_station_address = models.ForeignKey(Address, on_delete=models.SET_NULL)
    arrival_time = models.TimeField()
