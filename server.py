from flask import Flask, request, jsonify
from datetime import datetime
import os

app = Flask(_name_)

# Simulated DB for demo
vehicle_data_store = {}

@app.route('/api/vehicle_data', methods=['POST'])
def receive_vehicle_data():
    data = request.json
    vehicle_id = data.get('vehicle_id')
    lat = data.get('latitude')
    lng = data.get('longitude')
    timestamp = data.get('timestamp', datetime.utcnow().isoformat())

    if vehicle_id and lat and lng:
        vehicle_data_store[vehicle_id] = {
            'lat': lat,
            'lng': lng,
            'timestamp': timestamp
        }
        return jsonify({'status': 'success'}), 200
    else:
        return jsonify({'status': 'error', 'message': 'Invalid data'}), 400

if _name_ == "_main_":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)