import os
import pandas as pd
from flask import Flask, render_template, request, session
from werkzeug.utils import secure_filename

# アップロードフォルダのパス
UPLOAD_FOLDER = os.path.join('static', 'uploads')

# 許可する拡張子のセット
ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.secret_key = '94542eb06c77ff55' # 本番は.env に隠す

@app.route('/', methods=['GET', 'POST'])
def uploadfile():
    if request.method == 'POST':
        f = request.files.get('file')
        # ファイル名を安全にする
        data_filename = secure_filename(f.filename)
        # ファイルを保存
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],data_filename))
        # ファイルパスをセッションに保存
        session['upload_data_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'],data_filename)
        
        return render_template('index2.html')
    
    return render_template('index.html')

@app.route('/show_data')
def showData():
    # セッションからファイルパスを取得
    data_file_path = session.get('upload_data_file_path', None) # キーが存在しない場合は None
    # ファイルパスを読み込み、DataFrame に変換。encoding で文字コード指定
    uploaded_df = pd.read_csv(data_file_path, encoding='shift_jis')
    # 読み込んだ DataFrame を HTML テーブル形式に変換
    uploaded_df_html = uploaded_df.to_html() # escape=False
    return render_template('show_csv_data.html', data_var=uploaded_df_html)

if __name__ == '__main__':
    app.run(debug=True)