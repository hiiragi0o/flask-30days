from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quizzes.db' # SQLite DBの場所
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200), nullable=False)
    choice1 = db.Column(db.String(100), nullable=False)
    choice2 = db.Column(db.String(100), nullable=False)
    choice3 = db.Column(db.String(100), nullable=False)
    choice4 = db.Column(db.String(100), nullable=False)
    answer = db.Column(db.String(100), nullable=False)

# 初回だけDBを作る処理
with app.app_context():
    db.create_all() # テーブル作成

    # 初期データがなければ追加
    if Quiz.query.count() == 0:
        q1 = Quiz(
            question='Pythonのファイル拡張子は？',
            choice1='py', choice2='js', choice3='html', choice4='css',
            answer='py'
        )
        q2 = Quiz(
            question='HTMLの見出しタグは？',
            choice1='<p>', choice2='<h1>', choice3='<div>', choice4='<title>',
            answer='<h1>'
        )
        q3 = Quiz(
            question='Flaskは何のフレームワーク？',
            choice1='Web', choice2='AI', choice3='ゲーム', choice4='画像処理',
            answer='Web'
        )
        db.session.add_all([q1, q2, q3])
        db.session.commit()

# スタート画面
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz/<int:question_id>', methods=['GET', 'POST'])
def quiz(question_id): # 引数
    quiz = Quiz.query.get_or_404(question_id) # 現在の問題をDBから取得
    result = None
    answerd = False

    # 次の問題を取得（ID順で次）を計算
    next_quiz = Quiz.query.filter(Quiz.id > quiz.id).order_by(Quiz.id).first()
    next_id = next_quiz.id if next_quiz else None # 次がなければNone

    if request.method == 'POST':
        selected = request.form.get('choice')
        if selected == quiz.answer:
            result =  f"正解です！"
        else:
            # f-stringを使用して変数の値を埋め込む
            result =  f"不正解です。正しい回答は {quiz.answer} です"
        
        answerd = True # 回答済みにする

        return render_template(
            'quiz.html',
            quiz=quiz,
            result=result,
            answerd=answerd,
            next_id=next_id,
            next_quiz=next_quiz
        )

    # GET時
    return render_template(
        'quiz.html', 
        quiz=quiz, 
        answerd=answerd
    )

if __name__ == '__main__':
    app.run(debug=True)