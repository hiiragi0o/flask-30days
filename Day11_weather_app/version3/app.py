# OpenWeatherMap API から情報を取得して表示する
# Flask側は JSONレスポンスを返すAPI化
# フロント側は JavaScript（fetch）でデータ取得＆HTML更新
import os
from flask import Flask, jsonify, render_template, request
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

@app.route('/')
def index():
    return render_template('index.html', cities=cities)

@app.route('/get_weather', methods=['POST'])
def get_weather():
    city_name = request.json.get('city')

    if not city_name:
        return jsonify({'error': '都市が指定されていません。'}), 400

    # OpenWeatherMap API(現在の天気、5日間/3時間ごとの予報)
    weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&lang=ja&units=metric'
    forecast_url = f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_KEY}&lang=ja&units=metric'

    weather_res = requests.get(weather_url)
    forecast_res = requests.get(forecast_url)

    # エラーハンドリング
    if weather_res.status_code != 200 or forecast_res.status_code != 200:
        return jsonify({'error': '天気情報を取得できませんでした。'}), 500

    weather_data = weather_res.json()
    forecast_data = forecast_res.json()

    # 現在の天気から必要なデータを抽出
    current_weather = {
        'city': weather_data['name'],
        'temperature': weather_data['main']['temp'],
        'description': weather_data['weather'][0]['description'],
        'icon': weather_data['weather'][0]['icon']
    }

    # 5日間の天気（3時間ごとのデータ → 1日ごとにまとめる）
    forecasts = {}
    for item in forecast_data['list']:
        data_text = item['dt_txt'].split(" ")[0]  # "2025-10-12"
        if data_text not in forecasts:
            forecasts[data_text] = {
                'temp':[],
                'weather':[],
                'icons':[]
            }
        forecasts[data_text]['temp'].append(item['main']['temp'])
        forecasts[data_text]['weather'].append(item['weather'][0]['description'])
        forecasts[data_text]['icons'].append(item['weather'][0]['icon'])

    forecast_list = []
    # 平均気温と代表的な天気を抽出
    for date, info in forecasts.items():
        avf_temp = round(sum(info['temp']) / len(info['temp']), 1)
        desc = max(set(info['weather']), key=info['weather'].count)
        icon = info['icons'][len(info['icons']) // 2] # 中間のアイコンを代表として使う
        forecast_list.append({
            'date': date,
            'temp': avf_temp,
            'description': desc,
            'icon': icon
        })
    
    return jsonify({
        'current': current_weather,
        'forecast': forecast_list
    })


if __name__ == '__main__':
    app.run(debug=True)