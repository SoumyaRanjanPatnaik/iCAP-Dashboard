from django.db import models

class Woker(models.Model):
   id = models.IntegerField
   curr_bpm = models.FloatField
   height = models.FloatField
   avg_bpm = models.FloatField
   temperature = models.FloatField
   name = models.CharField
   location = models.CharField
   date = models.DateField(auto_now=False, auto_now_add=False)
   time = models.TimeField( auto_now=False, auto_now_add=False)