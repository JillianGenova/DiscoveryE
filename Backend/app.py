import time, json
from flask import Flask, request

app = Flask(__name__)

temp = 123

@app.route("/search", methods=["POST"])
def search_addr():
    data = request.get_json()
    dataStr = json.dumps(data)
    dataDict = json.loads(dataStr)
    print(dataDict['location']['state']['search'])
    return dataDict['location']['state']['search']

@app.route('/time')
def get_current_time():
    return {'time': time.time()}