# Google Books APIsで取得した任意の項目（json）を、HTMLに表示する
import os
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request
import requests

load_dotenv()
API_KEY = os.getenv('API_KEY')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    books_info = [] # ここに移動
    error = None

    if request.method == 'POST':
        # フォームから値を取得
        keyword = request.form.get('keyword', '').strip() # 両端の空白を削除
        authors = request.form.get('authors', '').strip()

        # キーワードも著者名もどちらも入力されていない場合
        if not keyword and not authors:
            error = "キーワードまたは著者名を入力してください。"
            return render_template('index.html', books_info=[], error=error)

        try:
            # # Google Books APIにリクエストを送り、検索結果を5つまで表示
            url = (
                f'https://www.googleapis.com/books/v1/volumes?q={keyword}'
                f'+inauthor:{authors}&startIndex=0&maxResults=5&key={API_KEY}'
                )
            response = requests.get(url, timeout=5) # 5秒でタイムアウト
            response.raise_for_status() # HTTPエラーを自動で例外に変換
            data = response.json()
            
            
            for item in data.get('items', []):
                volume = item.get('volumeInfo', {})
                image_links = volume.get('imageLinks', {}) # 画像はこの階層

                # 取り出したいキー（小さいサムネイル画像、サブタイトル、タイトル、著者名、出版日）
                books_data = {
                    'smallThumbnail': image_links.get('smallThumbnail'), 
                    'subtitle': image_links.get('subtitle'), 
                    'title': volume.get('title'), 
                    'authors': volume.get('authors'), 
                    'publishedDate': volume.get('publishedDate') 
                }
                books_info.append(books_data)

            # 結果が0件のとき
            if not books_info:
                error = f"検索結果が見つかりませんでした。"

        # ---- エラーハンドリング ----
        except requests.exceptions.RequestException as e:
            # APIリクエストエラーを処理
            error = f"APIリクエストエラーが発生しました: {e}"
        except Exception as e:
            # その他のエラーを処理
            error = f"予期せぬエラーが発生しました: {e}"
        
    return render_template('index.html', books_info=books_info, error=error)

if __name__ == '__main__':
    app.run(debug=True)