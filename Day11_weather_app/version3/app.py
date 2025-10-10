# 「都市名」によるAPIリクエスト
# OpenWeatherMap API から情報を取得してjsonで表示する
import os
from flask import Flask, Response, json, jsonify
from flask.cli import load_dotenv
import requests

load_dotenv() # .env を読み込む
API_KEY = os.getenv('API_KEY') # .envを使うために必要

app = Flask(__name__)

@app.route('/')
def index():
    # OpenWeatherMapのAPIで天気を取得する
    city_name = "Tokyo"  # 都市名
    api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&lang=ja&units=metric'
    response = requests.get(api_url)
    data = response.json()

    # エラーハンドリング追加
    if response.status_code != 200 or 'name' not in data:
        return jsonify({'error': data.get('message', 'APIリクエストに失敗しました')}), 500

    # 取得した天気データを整形
    weather_data = {
        'city': data['name'],
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'] 
    }

    # json.dumps を使い、Flask の Response で返す
    response_json = json.dumps(weather_data, ensure_ascii=False) # ensure_ascii=False で日本語をそのまま出力
    return Response(response_json, content_type='application/json; charset=utf-8')


if __name__ == '__main__':
    app.run(debug=True)