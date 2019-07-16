from celery import Celery
import time

worker = Celery('experiments',
    backend='redis://localhost',
    broker='redis://localhost')

@worker.task
def dummy():
    while True:
        print("working....")
        time.sleep(10)

