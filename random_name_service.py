from flask import Flask, jsonify
import random

app = Flask(__name__)

# Load names from files
with open('first_names.txt', 'r') as f:
    first_names = [line.strip() for line in f if line.strip()]

with open('last_names.txt', 'r') as f:
    last_names = [line.strip() for line in f if line.strip()]

@app.route('/person', methods=['GET'])
def get_random_person():
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    return jsonify({
        "first_name": first_name,
        "last_name": last_name
    })

if __name__ == '__main__':
    app.run()