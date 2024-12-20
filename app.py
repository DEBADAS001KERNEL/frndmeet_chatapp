from flask import Flask, render_template, request, jsonify
import random
import string
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# List to store messages
messages = []

# Function to generate a random user ID
def generate_user_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    user_id = generate_user_id()  # Generate a random user ID for anonymity
    messages.append({'user_id': user_id, 'message': message})
    return jsonify({"status": "Message sent"}), 200

@app.route('/get_messages', methods=['GET'])
def get_messages():
    return jsonify(messages)

if __name__ == "__main__":
    app.run(debug=True)
