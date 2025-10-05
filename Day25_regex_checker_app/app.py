import re
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    highlighted = None # ハイライト結果を入れる変数
    pattern = ""    # 初期値を空に設定
    text = ""       # 初期値を空に設定
    
    # options を定義
    options = {'ignorecase':False, 'multiline': False, 'dotall':False}

    if request.method == 'POST':
        pattern = request.form.get('pattern')
        text = request.form.get('text')

        # 正規表現のオプションを取得
        options['ignorecase'] = bool (request.form.get('ignorecase'))
        options['multiline'] = bool(request.form.get('multiline'))
        options['dotall'] = bool(request.form.get('dotall'))
        

        # 正規表現のオプションを設定
        flags = 0
        if options['ignorecase']:
            flags |= re.IGNORECASE
        if options['multiline']:
            flags |= re.MULTILINE
        if options['dotall']:
            flags |= re.DOTALL

        # 安全にコンパイルして使う
        try:
            matches = re.findall(pattern, text, flags=flags) # 正規表現でマッチする部分をすべて抽出
            result = matches if matches else 'マッチなし' # マッチがなければ「マッチなし」と表示
        
            # マッチ部分を黄色でハイライトする
            if matches:
                highlighted = re.sub(
                    pattern,
                    r'<mark>\g<0></mark>',
                    text,
                    flags=flags
                )
            else:
                highlighted = text  # マッチしないときはそのまま表示

        except re.error as e:
            result = f'正規表現エラー: {e}'
            highlighted = text # エラー時も元のテキストをそのまま表示

    return render_template(
        'index.html', 
        result=result, 
        options=options, 
        highlighted=highlighted,
        pattern=pattern,
        text=text
    )

if __name__ == '__main__':
    app.run(debug=True)