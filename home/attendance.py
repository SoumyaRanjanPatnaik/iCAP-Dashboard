from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from home import userfunc

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(userfunc.attendance, 'interval', hours = 6)
    scheduler.start()