# Flask アプリ基本構造
from flask import Flask, redirect, render_template, request, url_for
import sqlite3

app = Flask(__name__)

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
    app.run(debug=True)