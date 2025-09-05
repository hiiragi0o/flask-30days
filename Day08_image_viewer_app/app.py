import os
from flask import Flask, flash, redirect, render_template, request, send_from_directory, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './static/uploads/' # アップロードファイルを保存する場所
ALLOWED_EXTENSIONS = {'png' ,'jpg' ,'jpeg','gif'} # 許可されるファイル拡張子

app = Flask(__name__)
app.secret_key = 'dev_key_123' # flash メッセージのために必要
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True) # 念の為のエラー回避

# 拡張子を確認し、アップロードして、ファイルの URL にリダイレクトする関数
def allowed_file(filename):
    return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # POSTリクエストにファイル部分があるかどうかを確認する
        if 'file' not in request.files:
            flash('ファイルがありません') # 一時的なメッセージ（フラッシュメッセージ）を保存
            return redirect(request.url)
        file = request.files['file']

        # ユーザーがファイルを選択しない場合、ブラウザはファイル名のない空のファイルを送信します。 
        if file.filename == '':
            flash('ファイルが選択されていません')
            return redirect(request.url)
        
        # 許可されたファイルであれば
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename) # 必ずセキュリティを確保
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('アップロード成功')
            return redirect(url_for('download_file', name=filename))
        else:
            flash('許可されていないファイル形式です')
            return redirect(request.url)

    return render_template('upload.html')

@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)


if __name__ == '__main__':
    app.run(debug=True)