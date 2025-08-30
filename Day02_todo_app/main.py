from datetime import datetime
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

# DB を使用しない、簡易的なデータ保存
todos = [
    {'index':0,'task': "Pythonの基礎学習", 'detail': '変数、データ型、制御構造について学ぶ', 'time': '7/1 11:10', 'done': True},
    {'index':1,'task': "Webスクレイピング", 'detail': 'BeautifulSoupを使ってWebページから情報取得', 'time': '7/10 13:13', 'done': False},
    {'index':2,'task': "データベース連携", 'detail': 'SQLiteを使ったデータの保存と取得方法', 'time': '7/12 9:10', 'done': False},
    {'index':3,'task': "GUIアプリ作成", 'detail': 'Tkinterを使って簡単なGUIアプリを作る', 'time': '7/13 10:30', 'done': False}
]


# トップページ
@app.route('/')

# todosの値をindex.htmlへ渡し一覧表示
def index():
    return render_template('index.html', todos=todos)


# タスク追加ページ
@app.route('/add', methods = ['GET', 'POST'])

def add():
    # フォームのmethodがPOSTだった場合、フォームの各要素を取得しtodosリストに追加
    if request.method == 'POST':
        task = request.form['task']
        detail = request.form['detail']
        now = datetime.now()
        time = now.strftime('%m/%d %H:%M')

        # タスク名、タスク詳細、作成時間、完了ステータスの値をリストで保持
        todos.append({'index':len(todos), 'task': task, 'detail': detail, 'time': time, 'done': False})
        
        return redirect(url_for('index'))
    
    return render_template('add.html')


# タスク完了処理
@app.route('/complete/<index>')

# タスクのインデックスが一致するものを完了ステータスに変更して、一覧画面(/)にリダイレクト
def complete(index):
    todos[int(index)]['done'] = True
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)