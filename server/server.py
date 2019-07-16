from flask import Flask, request, jsonify

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

</pre></body></html>
"""

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

