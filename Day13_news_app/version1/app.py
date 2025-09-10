# News API からニュースを取得して辞書で表示する
import os
from dotenv import load_dotenv
from flask import Flask, jsonify
import requests

load_dotenv()
API_KEY = os.getenv('API_KEY')

app = Flask(__name__)

@app.route('/')
def index():
    # ビットコインに関するすべての記事を取得
    url = f'https://newsapi.org/v2/everything?q=bitcoin&apiKey={API_KEY}'
    response = requests.get(url)
    news = response.json()
    # 辞書で表示
    return jsonify(news)

if __name__ == '__main__':
    app.run(debug=True)