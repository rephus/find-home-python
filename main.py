#!/usr/bin/python

#http://flask.pocoo.org/
from flask import Flask, jsonify, render_template, request
import json
import time

app = Flask(__name__, static_folder='public', static_url_path='')

@app.route("/", methods=['GET'])
def index():
    return app.send_static_file('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug = True)
