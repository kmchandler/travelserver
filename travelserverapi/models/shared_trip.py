from django.db import models
from .user import User
from .trip import Trip


class SharedTrip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'trip'], name='unique_share_trip')
        ]
