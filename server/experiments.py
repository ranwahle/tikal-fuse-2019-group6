from celery import Celery
import time
import requests

worker = Celery('experiments',
                backend='redis://localhost',
                broker='redis://localhost')


@worker.task
def dummy():
    while True:
        print("working....")
        time.sleep(10)


@worker.task()
def attack_cart():
    url = "http://g6.fuse.tikal.io/cart"

    params = {}

    r = requests.get(url=url, params=params)

    data = r.json()

    # printing the output
    print("Response: %s" % str(data))
