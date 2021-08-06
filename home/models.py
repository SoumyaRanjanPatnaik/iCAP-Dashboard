from django.db import models
from django.utils import timezone
# Create your models here.


class Worker(models.Model):
    worker_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    location_of_work = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Log(models.Model):
    worker_id = models.ForeignKey(Worker, on_delete=models.CASCADE, blank=False, null=False)
    height = models.FloatField(max_length=50)
    avg_bpm = models.FloatField(max_length=50)
    curr_bpm = models.FloatField(max_length=50)
    # temperature = models.FloatField(max_length=50)
    fall = models.BooleanField(default=False)
    date = models.DateField(default=timezone.localdate) 
    time = models.TimeField(default=timezone.localtime) 