import os
from worker import *
from flask import Flask

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return "go to /add/int/int"

@app.route('/add/<a>/<b>',methods=['GET'])
def add_task(a,b):
    r = add(int(a),int(b))
    return f"go to /task/{ r.id }"

@app.route('/task/<taskid>', methods=['GET'])
def get_task(taskid):
    result = huey.result(taskid)
    return f"Result: { result }"

if __name__ == '__main__':
    os.system("huey_consumer.py worker.huey &")
    app.run(host='0.0.0.0',debug=False)
