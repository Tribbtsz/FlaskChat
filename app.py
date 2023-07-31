import os
import requests
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
load_dotenv()

API_KEY = os.getenv('API_KEY')
HEADERS = {
    'Authorization': f'Bearer {API_KEY}',
    'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
    'Content-Type': 'application/json'
}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    response = requests.post('https://api.aikey.one/v1/chat/completions', headers=HEADERS, json=data)
    return jsonify(response.json())


@app.route('/balance')
def balance():
    response = requests.get('https://api.aikey.one/dashboard/billing/subscription', headers=HEADERS)
    return jsonify(response.json())


@app.route('/usage')
def usage():
    response = requests.get('https://api.aikey.one/dashboard/billing/usage', headers=HEADERS)
    return jsonify(response.json())


if __name__ == '__main__':
    app.run(debug=True)
