from datetime import timedelta
import time

from django.db.models.query import QuerySet
from django.utils.timezone import localdate
from home.models import *

from django.http import response

def update_dashboard(workers, last_update):
	response_val = {}
	worker = Worker.objects.all()
	
	for row in worker:
		curr_id=row.worker_id
		response_val[str(curr_id)]={}
		try:
			latest_log = Log.objects.filter(worker_id=curr_id).order_by("-datetime")[0]
			if (timezone.localdate()!=latest_log.date):
				response_val.pop(str(curr_id))
				continue

			if (timezone.now()-latest_log.datetime)>timedelta(minutes=5):
				response_val[str(curr_id)]["status"]="Offline"
			else:
				response_val[str(curr_id)]["status"]="Online"
			response_val[str(curr_id)]["fall_detected"]=latest_log.fall
			response_val[str(curr_id)]["pulse"]={}
			response_val[str(curr_id)]["pulse"]["avg"]=latest_log.avg_bpm
			response_val[str(curr_id)]["pulse"]["curr"]=latest_log.curr_bpm
			response_val[str(curr_id)]["height"]=latest_log.height
		except Exception:
			print("Exception")
			response_val[str(curr_id)]={"ERROR":"No logs found"}
	return response_val

def update_model(data=None, addr = None):
	newLog = Log()
	newWorker = Worker
	newLog.worker_id = newWorker.objects.get(pk=addr)
	newLog.curr_bpm = data["pulse"]["curr"]
	newLog.avg_bpm = data["pulse"]["avg"]
	newLog.height = data["height"]
	newLog.fall = data["fall_detected"]
	newLog.save()
	last_attendance = Attendance.objects.filter(worker_id = curr_id).order_by("datetime")[0]	
	if(last_attendance.date!=timezone.localdate()):
		new_attendance = Attendance()
		new_attendance.worker_id=Worker.objects.get(pk=addr)
		new_attendance.Present=True
		new_attendance.save()
	


def attendance():
	for row in Worker:
		curr_id = row.worker_id		
		last_attendance = Attendance.objects.filter(worker_id = curr_id).order_by("datetime")[0]	
		if(last_attendance.date!=timezone.now()):
			temp_date = last_attendance.date+timedelta(1)
			curr_date = timezone.localdate()
			while(True):
				new_attendance = Attendance()
				new_attendance.worker_id=Worker.objects.filter(pk=curr_id)
				new_attendance.Present=False
				new_attendance.date = temp_date
				new_attendance.save()
				temp_date+=timedelta(days=1)
				if(temp_date==curr_date):
					break
			pass