import time

from django.db.models.query import QuerySet
from home.models import *

from django.http import response

def update_dashboard(workers, last_update):
	response_val = {
	}
	worker = Worker.objects.all()
	
	for row in worker:
		curr_id=row.worker_id
		response_val[str(curr_id)]={
			"addr": None,
			"data": {
				"fall_detected": None,
				"pulse": {
					"avg": None,
					"curr": None
				},
				"height": None
			}
		}
		pass
	response_val = {}
	status = "[ERROR]"
	for key in workers:
		if key in workers and int(time.time()) - last_update[key] <100:
			latest_log = Log.objects.all()[0]
			response_val[key] = workers[key]
			status = "[OK]"
			response_val["status"] = status
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

