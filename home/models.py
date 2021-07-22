from django.db import models
import datetime
# Create your models here.


class Worker(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    height = models.FloatField(max_length=50)
    avg_bpm = models.FloatField(max_length=50)
    curr_bpm = models.FloatField(max_length=50)
    temperature = models.FloatField(max_length=50)
    fall = models.BooleanField(default=False)
    date = datetime.datetime.now().date()
    time = datetime.datetime.now().time()

    def __str__(self):
        return self.name 

