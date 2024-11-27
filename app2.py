from flask import Flask, request, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# This global dictionary will hold the latest sensor values.
sensor_data = {
    'sensor1': 'No data for sensor1',
    'sensor2': 'No data for sensor2',
    'sensor3': 'No data for sensor3'
}

@app.route('/data', methods=['POST'])
def post_data():
    data = request.json
    print("Received POST request with:", data)  # Debug print
    if data:
        global sensor_data
        sensor_data['sensor1'] = data.get('sensor1', 'No data for sensor1')
        sensor_data['sensor2'] = data.get('sensor2', 'No data for sensor2')
        sensor_data['sensor3'] = data.get('sensor3', 'No data for sensor3')
        print("Emitting data:", sensor_data)  # Debug print
        socketio.emit('sensor_update', sensor_data)
        return "Data Received", 200
    else:
        return "No JSON data received", 400

@app.route('/')
def index():
    return render_template('display.html')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)