# GitHub APIでユーザーの情報をJSONで取得する
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # ユーザー名(hiiragi0o)のリポジトリ一覧を取得
    url = f'https://api.github.com/users/hiiragi0o/repos'
    response = requests.get(url)
    info = response.json()
    return jsonify(info)

if __name__ == '__main__':
    app.run(debug=True)