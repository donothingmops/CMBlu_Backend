# app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_points():
    # Example data, replace with your database query or business logic
    points = [
        {"id": 1, "x": 10, "y": 20, "z": 30},
        {"id": 2, "x": 15, "y": 25, "z": 35},
    ]
    return jsonify(points)

if __name__ == '__main__':
    app.run(debug=True)
