from celery import Celery
import time
import os
# import requests
# import json

worker = Celery('experiments',
                backend='redis://localhost',
                broker='redis://localhost')


@worker.task()
def attack_cart():
    # 03fef6ac-1896-4ce8-bd69-b798f85c6e0b
    # s = requests.Session()
    # cart_url = "http://g6.fuse.tikal.io/cart"
    #
    # request_body = {
    #     "id": "03fef6ac-1896-4ce8-bd69-b798f85c6e0b"
    # }
    # request_body_str = json.dumps(request_body)
    # headers = {'Content-Type': 'application/json; charset=UTF-8'}
    # print(request_body)
    # post_response = s.post(url=cart_url, data=request_body_str, headers=headers)
    # print("Add to cart %s" % post_response)
    #
    # r = s.get(url=cart_url)
    #
    # data = r.json()
    #
    # # printing the output
    # print("Cart get response: %s" % str(data))
    print("Running cart attack...")
    os.system("./run_cart_attack.sh")
    print("Running cart attack...")
