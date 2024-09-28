import json
import pandas as pd
from geopy.distance import geodesic
import psycopg2
from flask import Flask, request, jsonify

from .main import people_in_building

with open('../data-62743-2024-09-03.json', 'r', encoding='cp1251') as file:
    data = json.load(file)

app = Flask(__name__)

@app.route('/public', methods=['GET'])
def handle_post_1():
    response = {
        "message": "Alive"
    }

    return jsonify(data), 200

if __name__ == '__main__':
    app.run(host='localhost', port=4000)


