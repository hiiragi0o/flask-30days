# 最小限の「画像を指定サイズに変換して表示」機能
import io
from flask import Flask, render_template, request, send_file
from PIL import Image

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # ファイルの存在をチェック
        file = request.files['image']
        
        if not file:
            return 'ファイルがアップロードされていません', 400
        
        try:
            # リサイズ後のサイズ（整数に変換）
            width = int(request.form['width'])
            height = int(request.form['height'])
        except (ValueError, KeyError):
            return '幅と高さには整数を入力してください', 400

        # Pillowで開く
        img = Image.open(file)

        # リサイズ
        resized = img.resize((width, height))

        # メモリに保存して返す
        img_io =io.BytesIO()
        resized.save(img_io, format='PNG')
        img_io.seek(0)

        return send_file(img_io, mimetype='image/png')
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)