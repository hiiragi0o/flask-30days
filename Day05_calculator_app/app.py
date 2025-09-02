from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    num1 = float(data['num1'])
    num2 = float(data['num2'])
    operation = data['operation']

    result = None # GET アクセス時（フォーム送信前）の result を定義
    error = None

    try:
        if operation == 'add':
            result = num1 + num2
        elif operation == 'sub':
            result = num1 - num2
        elif operation == 'mul':
            result = num1 * num2
        elif operation == 'div':
            if num2 != 0 :
                result = num1 / num2
            else:
                error = 'ゼロ除算エラーです'
        else:
            error = '不明な演算です'

    except Exception as e:
        error = str(e)

    return jsonify({'result': result, 'error': error})

if __name__ == '__main__':
    app.run(debug=True)