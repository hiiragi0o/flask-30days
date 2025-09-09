# （外部API）ExchangeRate-APIでAPI取得してjsonで確認
import os
from flask import Flask, jsonify, jsonify, render_template
from flask.cli import load_dotenv
import requests

load_dotenv() # .env を読み込む
API_KEY = os.getenv('API_KEY') # .envを使うために必要


app = Flask(__name__)

@app.route('/')
def index():
    url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD'
    response = requests.get(url)
    data = response.json()
    return  jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)