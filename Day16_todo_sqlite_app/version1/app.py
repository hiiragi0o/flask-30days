from flask import Flask, render_template
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
    return render_template('base.html')

if __name__ == '__main__':
    with app.app_context():  # ← アプリケーションコンテキストを確保
        db.create_all()

        new_todo = Todo(title='todo 1', complete=False)
        db.session.add(new_todo)
        db.session.commit()
    app.run(debug=True)