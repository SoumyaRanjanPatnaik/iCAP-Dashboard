from datetime import timedelta
import time

from django.db.models.query import QuerySet
from django.utils.timezone import localdate
from home.models import *

from django.http import response

def update_dashboard(addr = None):
	response_val = {}
	worker = Worker.objects.all()
	
	for row in worker:
		curr_id=row.worker_id
		response_val[str(curr_id)]={}
		try:
			latest_log = Log.objects.filter(worker_id=curr_id).order_by("-datetime").first()
			if (abs(timezone.now()-latest_log.datetime)>timedelta(minutes=5)) and row.status == "Online":
				row.status = "Offline"
				if (timezone.localdate()!=latest_log.date):
					response_val.pop(str(curr_id))
					row.save()
					continue
				else:
					latest_log.pk = None
					latest_log.status=row.status
					latest_log.save()
			row.save()

			response_val[str(curr_id)]["status"]=row.status
			response_val[str(curr_id)]["fall_detected"]=latest_log.fall
			response_val[str(curr_id)]["pulse"]={}
			response_val[str(curr_id)]["pulse"]["avg"]=latest_log.avg_bpm
			response_val[str(curr_id)]["pulse"]["curr"]=latest_log.curr_bpm
			response_val[str(curr_id)]["height"]=latest_log.height
		except Exception:
			response_val[str(curr_id)]={"status":"Offline"}
	return response_val

def attendance():
	worker = Worker.objects.all()
	for row in worker:
		curr_id = row.worker_id
		last_attendance = Attendance.objects.filter(worker_id = curr_id).order_by("-date").first()
		if(last_attendance is None):
			new_attendance = Attendance()
			new_attendance.worker_id=Worker.objects.get(pk=curr_id)
			new_attendance.Present=False
			new_attendance.save()
		elif(last_attendance.date!=timezone.now()):
			curr_date = timezone.localdate()
			temp_date = last_attendance.date+timedelta(days=1)
			while(temp_date<curr_date):
				new_attendance = Attendance()
				new_attendance.worker_id=Worker.objects.get(pk=curr_id)
				new_attendance.Present=False
				new_attendance.date = temp_date
				new_attendance.save()
				temp_date+=timedelta(days=1)
		
def attendance_Present(addr):
	new_attendance = Attendance()
	new_attendance.worker_id=Worker.objects.get(pk=addr)
	new_attendance.Present=True
	new_attendance.save()

def update_model(data=None, addr = None):
	newLog = Log()
	newWorker = Worker
	curr_worker =  newWorker.objects.get(pk=addr)
	newLog.worker_id = curr_worker
	newLog.curr_bpm = data["pulse"]["curr"]
	newLog.avg_bpm = data["pulse"]["avg"]
	newLog.height = data["height"]
	newLog.fall = data["fall_detected"]
	newLog.status = "Online"
	newLog.save()
	curr_worker.status = "Online"
	curr_worker.save()

	last_attendance = Attendance.objects.filter(worker_id =addr).order_by("-date").first()	
	if(last_attendance == None):
		attendance_Present(addr)
		return
	if(last_attendance.date < timezone.localdate()):
		attendance()
	if(last_attendance.date!=timezone.localdate() or last_attendance.Present==False):
		new_attendance = Attendance()
		new_attendance.worker_id=Worker.objects.get(pk=addr)
		new_attendance.Present=True
		new_attendance.save()