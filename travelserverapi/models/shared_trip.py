from django.db import models
from .user import User
from .trip import Trip


class SharedTrip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.ForeignKey(Trip, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'board'], name='unique_share_trip')
        ]
