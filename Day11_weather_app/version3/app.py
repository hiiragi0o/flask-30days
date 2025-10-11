# OpenWeatherMap API から情報を取得してhtmlで表示する
from datetime import datetime
import os
from flask import Flask, Response, json, jsonify, render_template, request
from flask.cli import load_dotenv
import requests

load_dotenv() # .env を読み込む
API_KEY = os.getenv('API_KEY') # .envを使うために必要

app = Flask(__name__)

# 都市名で取得
cities = {
    '東京': 'Tokyo',
    '名古屋': 'Nagoya',
    '大阪': 'Osaka'
}

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    error = None

    if request.method == 'POST':
        city_name = request.form.get('area') # フォームから都市を取得

        # OpenWeatherMap API
        api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&lang=ja&units=metric'
        response = requests.get(api_url)
        data = response.json()

        # エラーハンドリング
        if response.status_code != 200 or 'main' not in data:
            error = data.get('message', '天気情報を取得できませんでした。')

        else:
            # 取得した天気データから必要なデータを抽出
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon']
            }
    
    return render_template('index.html', cities=cities, error=error, weather_data=weather_data)


if __name__ == '__main__':
    app.run(debug=True)