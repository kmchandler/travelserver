from django.db import models
from .user import User

class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=50)
