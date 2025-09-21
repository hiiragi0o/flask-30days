import io
import qrcode as qrcode_lib # 名前が被るので別名でインポート
from flask import Flask, render_template, request, send_file
from flask_qrcode import QRcode


app = Flask(__name__)
qrcode = QRcode(app) # テンプレートで qrcode タグを使えるようにする


@app.route('/', methods=['GET', 'POST'])
def index():
    # トップページ: URL入力フォーム + QRコード生成
    url = ''
    message = ''

    if request.method == 'POST':
        url = request.form.get('url', '').strip() # .strip()で空白や改行を取り除く
        if not url:
            message = 'URLを入力してください。'

    return render_template('index.html', url=url, message=message)


@app.route('/download', methods=['POST'])
def download():
    # 生成したQRコードをダウンロード
    url = request.form.get('url', '').strip()
    if not url:
        return 'URLがありません', 400
    
    # python の qrcode ライブラリを直接使用してPNGを生成
    img = qrcode_lib.make(url) # PIL.Image.Image オブジェクト
    buf = io.BytesIO() # メモリ上にバイナリデータを保持するためのバッファ
    img.save(buf, format='PNG')
    buf.seek(0) # バッファの先頭に戻る
    
    return send_file(buf,
                    mimetype='image/png',
                    as_attachment=True, # ダウンロードさせる
                    download_name='qrcode.png' # ダウンロード時のファイル名
                    )


if __name__ == '__main__':
    app.run(debug=True)