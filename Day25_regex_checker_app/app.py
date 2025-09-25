import re
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        pattern = request.form.get('pattern')
        text = request.form.get('text')

        try:
            matches = re.findall(pattern, text) # 正規表現でマッチする部分をすべて抽出
            result = matches if matches else 'マッチなし' # マッチがなければ「マッチなし」と表示
        except re.error as e:
            result = f'正規表現エラー: {e}'
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)