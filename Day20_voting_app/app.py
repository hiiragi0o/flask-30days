# 投票選択肢を管理する choices テーブルを作成
from flask import Flask, redirect, render_template, request, url_for
import sqlite3

app = Flask(__name__)

# app.py の init_db() を更新
def init_db():
    conn = sqlite3.connect('votes.db')
    c = conn.cursor()

    # 投票結果テーブル(votes) 更新
    # votes に choice_id を外部キーとして保持
    c.execute('''
        CREATE TABLE IF NOT EXISTS votes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            choice_id INTEGER NOT NULL,
            FOREIGN KEY(choice_id) REFERENCES choices(id)
        )
        ''')

    # 選択肢テーブル(choices)
    # choices テーブルに管理者が追加した選択肢を保存
    c.execute('''
        CREATE TABLE IF NOT EXISTS choices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()
    print("choicesテーブルを作成しました")

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/vote', methods=['POST'])
def vote():
    choice = request.form.get('choice')
    conn = sqlite3.connect('votes.db')
    c = conn.cursor()
    c.execute('INSERT INTO votes (choice) VALUES (?)', (choice,))
    conn.commit()
    conn.close()
    return redirect(url_for('result'))

@app.route('/result')
def result():
    conn = sqlite3.connect('votes.db')
    c = conn.cursor()
    # choice を取得、その行数（COUNT(*)）を取得、同じchoiceをグループ化
    c.execute('SELECT choice, COUNT(*) FROM votes GROUP BY choice')
    results = c.fetchall()  # [("A", 10), ("B", 5)]
    conn.close()
    return render_template('result.html', results=results)

if __name__ == '__main__':
    init_db() # テーブル作成
    app.run(debug=True)