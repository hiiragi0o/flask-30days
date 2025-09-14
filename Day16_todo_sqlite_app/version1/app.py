from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# /// = 相対パス、//// = 絶対パス（この場合は///なので相対パス）
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_v1.sqlite' # version1 のDBを作成
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# ToDoアイテム用のモデルクラス
# モデルには、ID、タイトル、そしてタスクが完了したかどうかを示すフラグの3つのエントリが必要
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

@app.route('/')
def index():
    # 全ての Todo を表示
    todo_list = Todo.query.all()
    print(todo_list)
    return render_template('base.html', todo_list=todo_list)

@app.route('/add', methods=['POST'])
def add():
    # アイテムを追加する
    title = request.form.get('title')
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:todo_id>')
def update(todo_id):
    # アイテムを更新する
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    # アイテムを削除する
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():  # ← アプリケーションコンテキストを確保
        db.create_all()
    app.run(debug=True)