import time, json
from flask import Flask, request
import location

app = Flask(__name__)

@app.route("/search", methods=["POST"])
def search_addr():
    data = request.get_json()
    dataStr = json.dumps(data)
    dataDict = json.loads(dataStr)
    output = ""
    
    print(list(dataDict['location']['state']['selectedFilters']))
    print(dataDict['location']['state']['params'])
    businesses = location.locationFeatureDriver(dataDict['location']['state']['params'], list(dataDict['location']['state']['selectedFilters']))
    #print(businesses)
    return json.dumps(businesses)

@app.route('/time')
def get_current_time():
    return {'time': time.time()}