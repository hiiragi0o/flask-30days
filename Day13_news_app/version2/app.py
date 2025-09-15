# HTML テンプレートを使って画面表示
import os
from dotenv import load_dotenv
from flask import Flask, render_template
from newsapi import NewsApiClient # requests の代わりに newsapi 公式ライブラリを使う

load_dotenv()
API_KEY = os.getenv('API_KEY')

app = Flask(__name__)
newsapi = NewsApiClient(api_key=API_KEY) # NewsApiClient のインスタンスを作成

@app.route('/')
def index():
    # アメリカのニュース top-headlines を取得
    top_headlines =  newsapi.get_top_headlines(language='en',country='us')
    articles = top_headlines['articles'] # 記事部分だけ取り出す
    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)