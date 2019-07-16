from flask import Flask, request, jsonify
from experiments import dummy, worker
# import experiments
# from celery import Celery

#worker = Celery('experiments',
#    backend='redis://localhost',
#    broker='redis://localhost')

app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
<html><body><pre>
Hello!
======
Welcome to the fuze api server

<a href="/api">/api</a>
<a href="/api/some_method">/api/some_mehod</a>
<a href="/api/experiments/status">/api/experiments/status</a>
<a href="/api/experiments/dummy/run">/api/experiments/dummy/run</a>

</pre></body></html>
"""

@app.route('/api/experiments/status')
def inspect_experiments():
    i = worker.control.inspect()
    return {
        'registered': i.registered(),
        'active': i.active(),
        'scheduled': i.scheduled(),
        'reserved': i.reserved(),
    }

@app.route('/api/experiments/dummy/run')
def run_dummy():
    dummy.delay()
    return { 'result': 'ok' }

@app.route('/api')
def api_example():
    return { 'this_is': { 'a': 'json' }, 'file': 42 }

@app.route('/api/<method>')
def api_method_example(method):
    return { 'this_is': { 'a': method }, 'file': 42 }

if __name__== '__main__':
    # PORT = os.environ.get(PORT)
    # HOST = os.environ.get(HOST)
    # print( HOST + ":" + (PORT))
    # app.run(host=HOST,port=int(PORT))
    app.run()

