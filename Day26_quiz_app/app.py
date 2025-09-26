from flask import Flask, render_template, request

app = Flask(__name__)

# 問題
quiz = {
    'question': 'Pythonのファイル拡張子は？',
    'choices': ['py', 'js', 'html', 'css'],
    'answer': 'py'
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        selected = request.form.get('choice')
        if selected == quiz['answer']:
            return f"正解です！"
        else:
            # f-stringを使用して変数の値を埋め込む
            return f"不正解です。正しい回答は {quiz['answer']} です"

    return render_template('index.html', quiz=quiz, result=result)

if __name__ == '__main__':
    app.run(debug=True)