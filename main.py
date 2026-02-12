import os
import sys
import time
from apscheduler.schedulers.background import BackgroundScheduler

def task():
    print("Success")

scheduler = BackgroundScheduler()
scheduler.add_job(task, "interval", seconds= 5)
scheduler.start()

while True:
    time.sleep(1)