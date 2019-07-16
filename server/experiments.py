from celery import Celery
import time
import requests
import json

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
    # 03fef6ac-1896-4ce8-bd69-b798f85c6e0b

    s = requests.Session()

    url = "http://g6.fuse.tikal.io/cart"
    body = {
        "id": "03fef6ac-1896-4ce8-bd69-b798f85c6e0b"
    }
    request_body = json.dumps(body)
    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    print(request_body)
    post_response = s.post(url=url, data=request_body, headers=headers)
    print("Add to cart %s" % post_response)

    params = {}

    r = s.get(url=url, params=params)

    data = r.json()

    # printing the output
    print("Cart get response: %s" % str(data))
