from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None # GET アクセス時（フォーム送信前）の result を定義
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operation = request.form['operation']

            if operation == 'add':
                result = num1 + num2
            elif operation == 'sub':
                result = num1 - num2
            elif operation == 'mul':
                result = num1 * num2
            elif operation == 'div':
                result = num1 / num2 if num2 != 0 else 'ゼロ除算エラーです'

        except Exception as e: # 例外処理
            result = f'エラー：{e}'
    return render_template('index.html', result=result )



if __name__ == '__main__':
    app.run(debug=True)