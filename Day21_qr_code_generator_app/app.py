from flask import Flask, render_template, request, send_file
from flask_qrcode import QRcode


app = Flask(__name__)
qrcode = QRcode(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/qrcode', methods=['GET'])
def get_qrcode():
    # /qrcode?data=<qrcode_data> を取得
    data = request.args.get('data', "")
    # 生成したQRコードのデータをPNG画像としてユーザーのブラウザに送り返す
    return send_file(qrcode(data, mode='raw'), mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True)