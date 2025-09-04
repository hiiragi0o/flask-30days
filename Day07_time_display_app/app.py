from flask import Flask, render_template
from flask_moment import Moment
from datetime import datetime

import pytz

app = Flask(__name__)
moment = Moment(app) # flask-momentのインスタンスを作成し、Flaskアプリケーションに登録

# 世界の主要都市とタイムゾーン
citiez = {
    'ロサンゼルス': 'America/Los_Angeles',
    'ニューヨーク': 'America/New_York',
    'ロンドン': 'Europe/London',
    'パリ': 'Europe/Paris',
    'シドニー': 'Australia/Sydney',
    '東京': 'Asia/Tokyo',
}

@app.route('/')
def index():
    world_times = {}
    for city, tz in citiez.items():
        # タイムゾーンを設定
        timezone = pytz.timezone(tz)
        # タイムゾーンで時刻を取得して、さらに正確な世界協定時UTCに変換（Moment.jsで動かすため）
        utc_now = datetime.now(timezone).astimezone(pytz.utc)
        # UTC時刻を各都市の時刻に変換
        world_times[city] = utc_now
    return render_template('index.html', world_times=world_times, citiez=citiez)

if __name__ == '__main__':
    app.run(debug=True)