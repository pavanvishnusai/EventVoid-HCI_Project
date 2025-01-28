from django.db import models
from datetime import datetime


class Events_List(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=1000)
    rules = models.TextField(default='')
    rating = models.FloatField(default=0.0)
    event_date = models.DateTimeField()

    def __str__(self):
        return self.title
    
# class Booking(models.Model):
#     event = models.CharField(max_length=200)
#     name = models.CharField(max_length=100) 
#     email = models.EmailField()
#     phone = models.CharField(max_length=20)

#     def __str__(self):
#         return self.event


class Participant(models.Model):
    event = models.CharField(max_length=200)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name