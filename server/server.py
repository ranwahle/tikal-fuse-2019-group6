from flask import Flask
from experiments import worker, attack_cart

app = Flask(__name__)


class Experiment:

    def __init__(self, task, desc):
        self.task = task
        self.desc = desc


experiment_manifest = {
    'attack_cart': Experiment(attack_cart, 'Attacks the cart'),
}


@app.route('/')
def hello_world():
    return """
<html><body><pre>
Hello!
======
Welcome to the fuze api server

<a href="/api/experiments">/api/experiments/status</a>
<a href="/api/experiments/status">/api/experiments/status</a>
<a href="/api/experiments/attack_cart/run">/api/experiments/dummy/run</a>

</pre></body></html>
"""


@app.route('/api/experiments/status')
def inspect_experiments():
    i = worker.control.inspect()
    return {
        'active': i.active()
    }


@app.route('/api/experiments')
def list_experiments():
    return {'experiments': [{'name': k, 'description': v.desc} for k, v in
                            experiment_manifest.items()]}


@app.route('/api/experiments/<name>/run')
def run_experiments(name):
    experiment = experiment_manifest.get(name)

    if not experiment:
        return "no experiment with name `{}`".format(name)

    experiment.task.delay()

    return {'result': 'ok'}


if __name__ == '__main__':
    app.run(host="0.0.0.0")
