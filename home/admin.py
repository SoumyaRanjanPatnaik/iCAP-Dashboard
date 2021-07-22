from django.contrib import admin
from .models import Worker
# Register your models here.


class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'height', 'avg_bpm', 'curr_bpm', 'temperature', 'fall', 'date', 'time')

admin.site.register(Worker, WorkerAdmin)

