from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) # GET アクセスでフォームを表示
def index():
    result = None # GET アクセス時（フォーム送信前）の result を定義

    if request.method == 'POST':
        text = request.form.get('text1')
        result = text[::-1] if text else None # 文字列を反転させる
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)