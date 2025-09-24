from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    count = None
    text = ''
    error = None # 初期値
    max_length = 100 # 最大文字数

    if request.method == 'POST':
        text = request.form.get('text', '')
        count = len(text)
        if count > max_length:
            error = f'最大文字数 {max_length} を超えています！'
            
    return render_template('index.html', count=count, text=text, error=error, max_length=max_length)

if __name__ == '__main__':
    app.run(debug=True)