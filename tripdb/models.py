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
