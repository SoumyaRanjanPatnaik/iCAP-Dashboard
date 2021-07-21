import time

from django.http import response

def update_dashboard(workers, last_update):
	response_val = {}
	status = "[ERROR]"
	for key in workers:
		if key in workers and int(time.time()) - last_update[key] >5:
			response_val[key] = workers[key]
			status = "[OK]"
			response_val["status"] = status
			last_update[key] = int(time.time())
	return response_val, last_update