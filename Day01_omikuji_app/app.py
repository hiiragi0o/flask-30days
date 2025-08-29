# HTMLファイルを読み込むために、render_templateモジュールをインポート
from flask import Flask, render_template
import random

# Flaskアプリケーションの作成
app = Flask(__name__)

# ルーティングの設定
@app.route('/') # ルートURLでも表示する
@app.route('/index/')

def omikuji():
    fortunes = ['大吉','中吉','小吉','凶', '大凶']
    return render_template('index.html', fortune=random.choice(fortunes))

# アプリケーションの実行
if __name__ == "__main__":
    app.run(debug=True)

    # python app.py コマンドで起動できる
