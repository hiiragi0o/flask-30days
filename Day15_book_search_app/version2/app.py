# Google Books APIsを使い書籍の検索結果をjsonで表示する
# 任意の項目を取得する
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
    data = response.json()

    # 取り出したいキー（小さいサムネイル画像、サブタイトル（あれば）、タイトル、著者名、出版日）
    fields_books = ['smallThumbnail', 'subtitle', 'title', 'authors', 'publishedDate']
    
    books_info = []
    for item in data.get('items', []):
        volume = item.get('volumeInfo', {})
        image_links = volume.get('imageLinks', {}) # 画像はこの階層
        books_data = {
            'smallThumbnail': image_links.get('smallThumbnail'), 
            'subtitle': image_links.get('subtitle'), 
            'title': volume.get('title'), 
            'authors': volume.get('authors'), 
            'publishedDate': volume.get('publishedDate') 
        }
        books_info.append(books_data)

    return jsonify(books_info)

if __name__ == '__main__':
    app.run(debug=True)