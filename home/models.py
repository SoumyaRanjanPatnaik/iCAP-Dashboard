from django.db import models

# Create your models here.


class Worker(models.Model):
    curr_bpm = models.TextField(max_length=50)
    height = models.FloatField(max_length=50)
    avg_bpm = models.FloatField(max_length=50)
    temperature = models.FloatField(max_length=50)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    fall = models.BooleanField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField( auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name 
