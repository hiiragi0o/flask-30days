from datetime import datetime
import os

from flask import Flask, redirect, render_template, request
from flask_migrate import Migrate
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
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
app.config["SECRET_KEY"] = os.urandom(24)

# SQL Alchemyのインスタンスのメソッド init_app に flaskインスタンス を渡して実行
db.init_app(app)

migrate = Migrate(app, db) # Migrateのインスタンスを作成

login_manager = LoginManager()
login_manager.init_app(app)

# Post用のモデルクラス
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(850), nullable=False)
    body =db.Column(db.String(300), nullable=False)
    tokyo_timezone = pytz.timezone('Asia/Tokyo')
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(tokyo_timezone))
    img_name = db.Column(db.String(300), nullable=True)

@app.route('/')
def index():
    posts = Post.query.all() # 全ての投稿を取得
    return render_template('index.html', posts=posts)

@app.route('/create', methods=['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')
    elif request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        post = Post(title=title, body=body) # PostgreSQLへ保存
        db.session.add(post) # PostgreSQLへ保存
        db.session.commit() # PostgreSQLへ保存
    return redirect('/')

@app.route('/<int:post_id>/update', methods=['GET','POST']) # idをキーにする
def update(post_id): # 引数
    post = Post.query.get(post_id) # 投稿を取得
    if request.method == 'POST':
        post.title = request.form.get('title') # post.が必要
        post.body = request.form.get('body')
        db.session.commit() # DB更新
        return redirect('/')

    else:
        return render_template('update.html', post=post) # GET でpost を表示

@app.route('/<int:post_id>/delete') # idをキーにする
def delete(post_id): # 引数
    post = Post.query.get(post_id)
    db.session.delete(post) # 削除
    db.session.commit() # DB更新
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)