# HTML テンプレートを使って画面表示
import os
from dotenv import load_dotenv
from flask import Flask, render_template
import requests

load_dotenv()
API_KEY = os.getenv('API_KEY')

app = Flask(__name__)

@app.route('/')
def index():
    # 日本 のニュース top-headlines を取得
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}'
    response = requests.get(url)
    articles = response.json()['articles'] # 記事部分だけ取り出す
    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)