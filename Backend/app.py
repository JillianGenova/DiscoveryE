import time
from flask import Flask, request

app = Flask(__name__)

temp = 123

@app.route("/search", methods=["POST"])
def search_addr():
    data = request.get_json()
    print(data)
    temp = 333
    return data

@app.route('/time')
def get_current_time():
    return {'time': time.time()}