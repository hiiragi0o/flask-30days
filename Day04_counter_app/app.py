import os
from flask import Flask, redirect, render_template, session, url_for
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv() # .env を読み込む

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY') # セッションを使うために必要
app.permanent_session_lifetime = timedelta(minutes=30) # セッションの有効期限


@app.route('/')
def index():
    # もし'session'に'count'がなければ、0で初期化
    if 'count' not in session:
        session['count'] = 0

    return render_template('index.html', count=session['count'])


@app.route('/increment')
def increment():
    # カウントアップ
    session['count'] += 1
    return redirect(url_for('index'))

@app.route('/decrement')
def decrement():
    # カウントダウン
    session['count'] -= 1
    return redirect(url_for('index'))


@app.route('/reset')
def reset():
    # カウントをリセット
    session['count'] = 0

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()