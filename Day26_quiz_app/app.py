from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

# 問題
quizzes = [
    {
    'question': 'Pythonのファイル拡張子は？',
    'choices': ['py', 'js', 'html', 'css'],
    'answer': 'py'
    },
    {
    'question': 'HTMLの見出しタグは？',
    'choices': ['<p>', '<h1>', '<div>', '<title>'],
    'answer': '<h1>'
    },
    {
    'question': 'Flaskは何のフレームワーク？',
    'choices': ['Web', 'AI', 'ゲーム', '画像処理'],
    'answer': 'Web'
    }
]

@app.route('/')
def index():
    # 最初の問題（0番目）にリダイレクト
    return redirect(url_for('quiz', question_index=0))

@app.route('/<int:question_index>', methods=['GET', 'POST'])
def quiz(question_index): # 引数
    if question_index >= len(quizzes):
        return 'クイズ終了！お疲れさまでした。'
    
    quiz = quizzes[question_index]
    result = None
    answerd = False

    if request.method == 'POST':
        selected = request.form.get('choice')
        if selected == quiz['answer']:
            result =  f"正解です！"
        else:
            # f-stringを使用して変数の値を埋め込む
            result =  f"不正解です。正しい回答は {quiz['answer']} です"
        
        answerd = True # 回答済みにする

        return render_template(
            'quiz.html',
            quiz=quiz,
            question_index=question_index,
            result=result,
            answerd=answerd,
            total=len(quizzes)
        )

    # GET時
    return render_template(
        'quiz.html', 
        quiz=quiz, 
        question_index=question_index,
        answerd=answerd,
        total=len(quizzes)
    )

if __name__ == '__main__':
    app.run(debug=True)