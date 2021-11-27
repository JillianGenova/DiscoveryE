import time, json
from flask import Flask, request
import location

app = Flask(__name__)

temp = 123

@app.route("/search", methods=["POST"])
def search_addr():
    data = request.get_json()
    dataStr = json.dumps(data)
    dataDict = json.loads(dataStr)
    output = ""
    print(dataDict['location']['state']['params'])
    businesses = location.locationFeatureDriver(dataDict['location']['state']['params'], ["food", "clothes"])
    for i in businesses:
        output = output + i[0] + " "
    return output

@app.route('/time')
def get_current_time():
    return {'time': time.time()}