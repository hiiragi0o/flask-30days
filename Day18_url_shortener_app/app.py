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

@app.route('/<id>')
def url_redirect(id): # 引数
    conn = get_db_connection()

    original_id = hashids.decode(id)# idをもとのidに変換

    # もとのidが存在する場合
    if original_id:
        original_id = original_id[0] # もとのidを取得
        # もとのURLをDBから取得
        url_data = conn.execute('SELECT original_url, clicks FROM urls'
                                ' WHERE id = (?)', (original_id,)
                                ).fetchone()
        original_url = url_data['original_url']
        clicks = url_data['clicks'] # クリック数を取得

        # クリック数を1増やす
        conn.execute('UPDATE urls SET clicks = ? WHERE id = ?',
                    (clicks+1, original_id))

        conn.commit()
        conn.close()
        return redirect(original_url)
    
    # 無効なURLの場合
    else:
        flash('無効な短縮 URL です')
        return redirect(url_for('index'))

@app.route('/stats')
def stats():
    conn = get_db_connection()
    # urls テーブルから id, created, original_url, clicks カラムを取得
    db_urls = conn.execute('SELECT id, created, original_url, clicks FROM urls'
                            ).fetchall()
    
    conn.close()

    urls = []
    for url in db_urls:
        url = dict(url) # sqlite3.Row オブジェクトを辞書に変換
        url['short_url'] = request.host_url + hashids.encode(url['id'])
        urls.append(url) # urls リストに追加

    return render_template('stats.html', urls=urls)

if __name__ == '__main__':
    app.run(debug=True)