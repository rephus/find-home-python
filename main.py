#!/usr/bin/python

#http://flask.pocoo.org/
from flask import Flask, jsonify, render_template, request
import json
import time
from flask import Response

from db.stations import Stations

stationsDb = Stations()

app = Flask(__name__, static_folder='public', static_url_path='')

@app.route("/", methods=['GET'])
def index():
    return app.send_static_file('index.html')

@app.route("/stations", methods=['GET'])
def stations():

    #TODO move this converter to Stations model
    all_stations = [{
                     "id": s[0], "name": s[1], "zone": s[2],
                     "postalCode":  s[3], "lat":  s[4], "lon":  s[5]
                     } for s in stationsDb.all()]
    response = Response(json.dumps(all_stations),  mimetype='application/json')
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug = True)
