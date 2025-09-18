import sqlite3
from hashids import Hashids
from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ad7841f2c2251a0e798940706579d883' # 本来は .env

# 4文字に変換する設定
hashids = Hashids(min_length=4, salt=app.config['SECRET_KEY']) # salt はハッシュを安全にするための追加情報

# データベースファイルへの接続
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db_connection() # DB接続

    if request.method == 'POST':
        url = request.form['url']

        if not url:
            flash('URLを入力してください！')
            return redirect(url_for('index'))
        
        # もとのURLをDBに追加。urls テーブルの original_url カラムに値を追加する
        url_data = conn.execute('INSERT INTO urls (original_url) VALUES (?)', (url,))

        conn.commit()
        conn.close()

        url_id = url_data.lastrowid # id 取得
        hashid = hashids.encode(url_id) # id を文字列に変換
        short_url = request.host_url + hashid # ホストURLとhashidを組み合わせる

        return render_template('index.html', short_url=short_url)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)