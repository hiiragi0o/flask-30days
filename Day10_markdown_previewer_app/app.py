from flask import Flask, render_template, request
import markdown

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # 値の初期化
    markdown_text = ""
    html_preview = ""

    # POSTリクエストがあった場合、フォームデータを取得
    if request.method == 'POST':
        markdown_text = request.form.get('markdown_text', '')
        # MarkdownをHTMLに変換
        html_preview = markdown.markdown(markdown_text)
    return render_template('index.html',
                            markdown_text=markdown_text,
                            html_preview=html_preview)

if __name__ == '__main__':
    app.run(debug=True)