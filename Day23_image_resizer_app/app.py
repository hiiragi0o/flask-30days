# 最小限の「画像を指定サイズに変換して表示」機能
import io
import os
from flask import Flask, render_template, request, send_file, url_for
from PIL import Image, ImageFilter

app = Flask(__name__)

# 保存先のフォルダ
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    processed_image_url = None

    if request.method == 'POST':
        # ファイルの存在をチェック
        file = request.files['image']
        
        if not file:
            return 'ファイルがアップロードされていません', 400
        
        # Pillowで開く
        img = Image.open(file)

        # 操作の種類を取得
        action = request.form.get('action', 'resize')

        try:
            # リサイズ後のサイズ（整数に変換）
            width = int(request.form.get('width', 200))
            height = int(request.form.get('height', 200))
        except (ValueError, KeyError):
            return '幅と高さには整数を入力してください', 400

        # 各処理の分岐
        if action == 'resize':
            resized = img.resize((width, height)) # リサイズ
        elif action == 'thumbnail':
            img.thumbnail((width, height)) # サムネイル
        elif action == 'blur':
            img = img.filter(ImageFilter.BLUR) # ぼかし
        elif action == 'sharpen':
            img = img.filter(ImageFilter.SHARPEN) # シャープ化
        elif action == 'rotate':
            img = img.rotate(90) # 90度回転
        elif action == 'flip':
            img = img.transpose(Image.FLIP_LEFT_RIGHT) # 左右反転

        # 保存先パス
        save_path = os.path.join(UPLOAD_FOLDER, 'result.png')
        img.save(save_path)

        # ブラウザに渡すURL
        processed_image_url = url_for('static', filename='uploads/result.png')
    
    return render_template('index.html', img_url=processed_image_url)

if __name__ == '__main__':
    app.run(debug=True)