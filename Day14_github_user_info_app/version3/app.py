# GitHub APIでユーザーの情報をJSONで取得し、画面に表示する
from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)

# 英語キー -> 日本語キー
FIELDS_JA = {
    "avatar_url": "アイコン",
    "login": "ユーザー名",
    "html_url": "プロフィールURL",
    "bio": "自己紹介文",
    "repo_names": "リポジトリ名"
}

@app.route('/', methods=['GET', 'POST'])
def index():
    data_display = []
    data_user = {}
    username = None
    error = None

    if request.method == 'POST':
        username = request.form.get('username') # フォーム入力を取得

        if not username:
            error = 'ユーザー名を入力してください。'
        else:
            try:
                ''' ユーザー情報 '''
                response_user = requests.get(f'https://api.github.com/users/{username}') # これは辞書を返す{}
                response_user.raise_for_status()# ステータスコードが200(成功)以外の場合はエラーを発生させる
                data_user = response_user.json()

                # 取り出したいキー
                # アイコン、ユーザー名、プロフィールURL、自己紹介文
                fields_user = ["avatar_url", "login", "html_url", "bio"]

                # Pythonの辞書内包表記でまとめて取り出す
                data_user = {key : data_user.get(key) for key in fields_user}

                ''' リポジトリのタイトル一覧 '''
                response_repo = requests.get(f'https://api.github.com/users/{username}/repos')  # これは辞書を要素とするリストを返す[{},{} ...]
                response_repo.raise_for_status()
                data_repo = response_repo.json()

                # Pythonのリスト内包表記で "name" の値を取り出す
                data_repo = [repo.get("name") for repo in data_repo]

                ''' ユーザー情報とリポジトリ名リストを一つの辞書にまとめる '''
                data_user["repo_names"] = data_repo

                ''' APIから取得した data_user を日本語キーに変換 '''
                data_user = {jp_key: data_user.get(en_key) for en_key,jp_key in FIELDS_JA.items()}
                # { "アイコン": "http...", のようになる

                ''' テンプレート用に (data, name_ja) のリストを作る '''
                data_display = [(name_ja, data) for name_ja, data in data_user.items() if data] # data がある場合のみ追加
                
            # HTTPエラー処理(json でなく、変数 error にメッセージを入れてhtmlで返す)
            except requests.exceptions.HTTPError as e:
                if e.response.status_code == 404:
                    error = f'ユーザー "{username}" は見つかりません。'
                else:
                    error = f'GitHub API エラー: {e}'
            except Exception as e:
                error = f'予期せぬエラー: {e}'
            
    return render_template('index.html', 
                            data_display=data_display,
                            data_user=data_user,
                            username=username,
                            error=error)


if __name__ == '__main__':
    app.run(debug=True)