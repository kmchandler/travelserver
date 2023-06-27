from django.db import models
from . import Itinerary

class Note(Itinerary):
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
    note = models.TextField()
