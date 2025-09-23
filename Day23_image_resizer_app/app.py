# 最小限の「画像を指定サイズに変換して表示」機能
import io
from flask import Flask, render_template, request, send_file
from PIL import Image, ImageFilter

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
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
        elif action == 'format_convert':
            # JPEG に変換して保存する例（品質85）
            img_io = io.BytesIO()
            img = img.convert('RGB') # JPEG はRGB必須
            img.save(img_io, format='JPEG', quality=85) # 形式を指定して保存
            img_io.seek(0)
            return send_file(img_io, mimetype='image/jpeg')
        

        # それ以外はPNGで返す
        img_io = io.BytesIO()
        img.save(img_io, format='PNG')
        img_io.seek(0)
        return send_file(img_io, mimetype='image/png')
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)