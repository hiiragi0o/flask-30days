import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
from newsapi import NewsApiClient # requests の代わりに newsapi 公式ライブラリを使う

load_dotenv()
API_KEY = os.getenv('API_KEY')

app = Flask(__name__)
newsapi = NewsApiClient(api_key=API_KEY) # NewsApiClient のインスタンスを作成

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        keyword = request.form['keyword']
        news = newsapi.get_everything(q=keyword, language='en', sort_by='relevancy') # 関連度順にソート
        articles = news['articles'] # 記事部分だけ取り出す
        return render_template('index.html', articles=articles, keyword=keyword)

    else:
        # keyword がない時 top-headlines を取得
        top_headlines =  newsapi.get_top_headlines(language='en',country='us')
        articles = top_headlines['articles'] # 記事部分だけ取り出す
        return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)