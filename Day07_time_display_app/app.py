from flask import Flask, render_template
from flask_moment import Moment
from datetime import datetime

import pytz

app = Flask(__name__)
moment = Moment(app) # flask-momentのインスタンスを作成し、Flaskアプリケーションに登録

@app.route('/')
def index():
    # 現在のUTC時刻を取得
    utc_now = datetime.now(pytz.utc) # 世界協定時　+00:00
    # JSTタイムゾーンを設定
    jst = pytz.timezone('Asia/Tokyo')
    # UTC時刻をJSTに変換
    jst_now = utc_now.replace(tzinfo=pytz.utc).astimezone(jst)
    return render_template('index.html', current_time=jst_now)


if __name__ == '__main__':
    app.run(debug=True)