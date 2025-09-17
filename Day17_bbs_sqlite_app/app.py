from datetime import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import pytz

app = Flask(__name__)

# SQL Alchemyのインスタンスを作成
db = SQLAlchemy()
DB_INFO = {
    'user': 'ys', # pgAdmin4 で設定した内容
    'password': '',
    'host': 'localhost',
    'name': 'postgres'
}
# データベースの接続情報の文字列を作成
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg://{user}:{password}@{host}/{name}'.format(**DB_INFO)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
# SQL Alchemyのインスタンスのメソッド init_app に flaskインスタンス を渡して実行
db.init_app(app)

# Post用のモデルクラス
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(850), nullable=False)
    body =db.Column(db.String(300), nullable=False)
    tokyo_timezone = pytz.timezone('Asia/Tokyo')
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(tokyo_timezone))

@app.route('/')
def index():
    posts =[
        {
        'title': '記事のタイトル',
        'body': '記事の内容',
        'created_at': '2020-01-01'
    },
    {
        'title': '記事のタイトル2',
        'body': '記事の内容2',
        'created_at': '2020-01-02'
    },
    {
        'title': '記事のタイトル3',
        'body': '記事の内容3',
        'created_at': '2020-01-03'
    }
    ]
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)