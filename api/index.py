import json
import pandas as pd
from geopy.distance import geodesic
import psycopg2
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

def load_json_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data

json_file_path = os.path.join(os.path.dirname(__file__), '../public/data-62743-2024-09-03.json')
json_data = load_json_data(json_file_path)

@app.route('/public', methods=['GET'])
def handler():
    response = {
        "message": "Alive"
    }
    return jsonify(response), 200

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(json_data), 200


def handler(event, context):
    return app(event, context)
