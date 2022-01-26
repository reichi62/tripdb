from django.db import models


# Create your models here.
class Trip(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10)
    start_date = models.DateField()
    duration = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Day(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()
    trip_id = models.ForeignKey(Trip, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
