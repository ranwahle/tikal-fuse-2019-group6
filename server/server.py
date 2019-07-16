from flask import Flask
from experiments import dummy, worker

app = Flask(__name__)

class Experiment():

    def __init__(self, task, desc):
        self.task = task
        self.desc = desc

experiment_manifest = {
    'dummy': Experiment(dummy, 'A dummy task'),
}


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
        #'registered': i.registered(),
        'active': i.active(),
        #'scheduled': i.scheduled(),
        #'reserved': i.reserved(),
    }

@app.route('/api/experiments')
def list_experiments():
    return { 'experiments': [ { 'name': k, 'description': v.desc } for k, v in
            experiment_manifest.items() ] }

@app.route('/api/experiments/<name>/run')
def run_experiments(name):

    experiment = experiment_manifest.get(name)

    if not experiment:
        return "no experiment with name `{}`".format(name)

    experiment.task.delay()

    return { 'result': 'ok' }

@app.route('/api')
def api_example():
    return {'this_is': {'a': 'json'}, 'file': 42}

@app.route('/api/<method>')
def api_method_example(method):
    return {'this_is': {'a': method}, 'file': 42}

if __name__ == '__main__':
    app.run(host="0.0.0.0")
