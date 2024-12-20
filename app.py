from flask import Flask, render_template, request  # Import 'request'
from flask_socketio import SocketIO, emit
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app, cors_allowed_origins="*")

# Track connected users
connected_users = set()

@app.route('/')
def index():
    return render_template('index.html')

# Handle incoming messages
@socketio.on('message')
def handle_message(data):
    emit('new_message', data, broadcast=True, include_self=False)

# Handle user connections
@socketio.on('connect')
def handle_connect():
    global connected_users
    connected_users.add(request.sid)  # Use request.sid to identify the user session
    print(f"User connected: {request.sid}")

# Handle user disconnections
@socketio.on('disconnect')
def handle_disconnect():
    global connected_users
    connected_users.remove(request.sid)  # Remove user from the set
    if len(connected_users) == 0:
        print("All users left. Clearing messages.")
        # Logic to clear messages if implemented
    print(f"User disconnected: {request.sid}")

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=False)
