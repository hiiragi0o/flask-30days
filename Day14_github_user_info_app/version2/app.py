# ユーザーの情報から指定の項目を取得（アイコン、ユーザー名、プロフィールURL、自己紹介文）
# リポジトリ名の一覧[リスト]を取得
# ２つを１つの辞書にまとめる
# エラーハンドリング追加
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    
    try:
        ''' ユーザー情報 '''
        response_user = requests.get('https://api.github.com/users/hiiragi0o') # これは辞書を返す{}
        response_user.raise_for_status()# ステータスコードが200(成功)以外の場合はエラーを発生させる
        data_user = response_user.json()

        # 取り出したいキー
        # アイコン、ユーザー名、プロフィールURL、自己紹介文
        fields_user = ["avatar_url", "login", "html_url", "bio"]

        # Pythonの辞書内包表記でまとめて取り出す
        data_user = {key : data_user.get(key) for key in fields_user}

        ''' リポジトリのタイトル一覧 '''
        response_repo = requests.get('https://api.github.com/users/hiiragi0o/repos')  # これは辞書を要素とするリストを返す[{},{} ...]
        response_repo.raise_for_status()
        data_repo = response_repo.json()

        # Pythonのリスト内包表記で "name" の値を取り出す
        data_repo = [repo.get("name") for repo in data_repo]

        ''' ユーザー情報とリポジトリ名リストを一つの辞書にまとめる '''
        data_user["repo_names"] = data_repo

        return jsonify(data_user)

    except requests.exeptions.RequestException as e:
        # APIリクエストエラーを処理
        return jsonify({"error" : f"APIリクエストエラーが発生しました:{e}"}),500
    except Exception as e:
        # その他のエラーを処理
        return jsonify({"error" : f"予期せぬエラーが発生しました:{e}" }),500


if __name__ == '__main__':
    app.run(debug=True)