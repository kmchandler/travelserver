from django.db import models
from . import ItineraryItem

class Note(ItineraryItem):
    itinerary_item = models.ForeignKey(ItineraryItem, on_delete=models.CASCADE)
    note = models.TextField()
