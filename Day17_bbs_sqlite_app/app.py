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

# アップロードを許可する拡張子のリスト
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# user 識別のため必須
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id)) # 引数に文字列がくるため整数型に変換

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)


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
# @login_required
def create():
    if request.method == 'GET':
        return render_template('create.html')
    
    elif request.method == 'POST':
        file = request.files['img'] # ファイルを取得
        filename = file.filename # ファイル名を取得

        if not allowed_file(filename):
            return '許可されていないファイル形式です。', 400
        
        img_name = os.path.join(app.static_folder, 'img', filename) # パスを作成
        file.save(img_name) # 保存

        title = request.form.get('title')
        body = request.form.get('body')
        post = Post(title=title, body=body, img_name=filename)
        db.session.add(post)
        db.session.commit()
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

@app.route('/<int:post_id>/readmore')
def readmore(post_id):
    post = Post.query.get(post_id)
    return render_template('readmore.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)