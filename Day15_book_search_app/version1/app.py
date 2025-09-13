# Google Books APIsを使い書籍の検索結果をjsonで表示する
import os
from dotenv import load_dotenv
from flask import Flask, jsonify
import requests

load_dotenv()
API_KEY = os.getenv('API_KEY')

app = Flask(__name__)

@app.route('/')
def index():
    # 「ハリー・ポッター　ローリング」の検索結果を2つまで表示
    url = f'https://www.googleapis.com/books/v1/volumes?q=ハリー・ポッター+inauthor:ローリング&startIndex=0&maxResults=2&key={API_KEY}'
    response = requests.get(url)
    books = response.json()
    return jsonify(books)

if __name__ == '__main__':
    app.run(debug=True)