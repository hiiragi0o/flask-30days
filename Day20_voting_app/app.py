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

@app.route("/")
def index():
    # 選択肢を表示
    conn = sqlite3.connect('votes.db')
    c = conn.cursor()
    c.execute('SELECT * FROM choices')
    choices = c.fetchall() # [(1, "A"), (2, "B"), ...]
    conn.close()
    return render_template("index.html", choices=choices)

@app.route('/vote', methods=['POST'])
def vote():
    # 投票処理を選択肢ID対応に変更
    choice_id = request.form.get('choice_id')
    conn = sqlite3.connect('votes.db')
    c = conn.cursor()
    c.execute('INSERT INTO votes (choice_id) VALUES (?)', (choice_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('result'))

@app.route('/result')
def result():
    conn = sqlite3.connect('votes.db')
    c = conn.cursor()
    c.execute('''
        SELECT choices.name, COUNT(votes.id)
        FROM choices
        LEFT JOIN votes ON votes.choice_id = choices.id
        GROUP BY choices.id
    ''')
    # 結果表示を選択肢名で集計
    # choices.name ごとに votes.id を集計
    # LEFT JOIN で votes テーブルを結合

    results = c.fetchall()  # [("A", 10), ("B", 5)]
    conn.close()
    return render_template('result.html', results=results)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    conn = sqlite3.connect('votes.db')
    c = conn.cursor()
    if request.method == 'POST':
        new_choice = request.form.get('new_choice')
        # 新しい選択肢を choices テーブルに追加
        if new_choice:
            # 重複を避けるために INSERT OR IGNORE を使用
            c.execute('INSERT OR IGNORE INTO choices (name) VALUES (?)', (new_choice,))
            conn.commit()
    # choices テーブルから全選択肢を取得
    c.execute('SELECT * FROM choices')
    choices = c.fetchall() # [(1, "A"), (2, "B"), ...]
    conn.close()
    return render_template('admin.html', choices=choices)

# 選択肢を編集するルート
@app.route('/admin/edit/<int:choice_id>', methods=['GET', 'POST'])
def edit_choice(choice_id):
    conn = sqlite3.connect('votes.db')
    c = conn.cursor()

    if request.method == 'POST':
        new_name = request.form.get('new_name')
        if new_name:
            c.execute('UPDATE choices SET name = ? WHERE id = ?', (new_name, choice_id))
            conn.commit()
            conn.close()
            return redirect('/admin')

    # GETリクエストの場合は編集フォームを表示
    c.execute('SELECT name FROM choices WHERE id = ?', (choice_id,))
    # fetchall() を使わず、 fetchone() → [0] で中身の文字だけ取り出す
    choice = c.fetchone()
    conn.close()
    return render_template('edit_choice.html', choice_id=choice_id, choice_name=choice[0])

# 選択肢を削除するルート
@app.route('/admin/delete/<int:choice_id>', methods=['POST'])
def delete_choice(choice_id):
    conn = sqlite3.connect('votes.db')
    c = conn.cursor()
    c.execute('DELETE FROM choices WHERE id = ?', (choice_id,))
    conn.commit()
    conn.close()
    return redirect('/admin')

if __name__ == '__main__':
    init_db() # テーブル作成
    app.run(debug=True)