from django.contrib import admin
from .models import *
# Register your models here.


class WorkerAdmin(admin.ModelAdmin):
    list_display = ('worker_id','name', 'location_of_work', )

class LogsAdmin(admin.ModelAdmin):
    list_display = ('worker_id', 'height', 'avg_bpm', 'curr_bpm', 'fall', 'date', 'time')

admin.site.register(Worker, WorkerAdmin)
admin.site.register(Log, LogsAdmin)

