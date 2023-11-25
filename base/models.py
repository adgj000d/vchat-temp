from django.db import models

# Create your models here.

class RoomDetails(models.Model):
    roomName = models.CharField(max_length=100)
    roomPassword = models.CharField(max_length=100)