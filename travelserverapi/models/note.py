from django.db import models
from . import ItineraryItem

class Note(ItineraryItem):
    itinerary_item = models.ForeignKey(ItineraryItem, related_name="note_here", on_delete=models.CASCADE)
    note_info = models.TextField()
