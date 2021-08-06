from datetime import timedelta
import time

from django.db.models.query import QuerySet
from home.models import *

from django.http import response

def update_dashboard(workers, last_update):
	response_val = {}
	worker = Worker.objects.all()
	
	for row in worker:
		curr_id=row.worker_id
		response_val[str(curr_id)]={}
		# try:
		# 	latest_log = Log.objects.filter(worker_id=curr_id)[0]
		# 	response_val[str(curr_id)]["fall_detected"]=latest_log.fall
		# 	response_val[str(curr_id)]["pulse"]={}
		# 	response_val[str(curr_id)]["pulse"]["avg"]=latest_log.avg_bpm
		# 	response_val[str(curr_id)]["pulse"]["curr"]=latest_log.curr_bpm
		# 	response_val[str(curr_id)]["height"]=latest_log.height
		# 	print(latest_log.datetime-datetime.now())
		# 	if (latest_log.datetime-datetime.now())>timedelta(minutes=5):
		# 		response_val[str(curr_id)]["Status"]="Offline"
		# except Exception:
		# 	response_val[str(curr_id)]={"ERROR":"No logs found"}
		latest_log = Log.objects.filter(worker_id=curr_id)[0]
		response_val[str(curr_id)]["fall_detected"]=latest_log.fall
		response_val[str(curr_id)]["pulse"]={}
		response_val[str(curr_id)]["pulse"]["avg"]=latest_log.avg_bpm
		response_val[str(curr_id)]["pulse"]["curr"]=latest_log.curr_bpm
		response_val[str(curr_id)]["height"]=latest_log.height
		if (timezone.localtime()-latest_log.datetime).total_seconds()/60>5:
			response_val[str(curr_id)]["status"]="Offline"
		else:
			response_val[str(curr_id)]["status"]="Online"
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

