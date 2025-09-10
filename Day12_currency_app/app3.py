# 入力した値、選択した通貨を円に換算して表示
import os
from flask import Flask, render_template, request
from flask.cli import load_dotenv
import requests

load_dotenv()
API_KEY = os.getenv('API_KEY')

app = Flask(__name__)

# 通貨コード -> 日本語名 辞書（日本円以外）
CURRENCY_NAMES_JA = {
    "USD": "米ドル",
    "EUR": "ユーロ",
    "GBP": "英ポンド",
    "AUD": "豪ドル",
    "CAD": "カナダドル",
    "CHF": "スイスフラン",
    "CNY": "中国人民元",
    "HKD": "香港ドル",
    "KRW": "韓国ウォン",
    "INR": "インドルピー",
    "TWD": "台湾ドル",
    "THB": "タイバーツ",
    "VND": "ベトナムドン",
    "BRL": "ブラジルレアル",
    "MXN": "メキシコペソ",
    "ZAR": "南アフリカランド",
    "RUB": "ロシアルーブル",
    "SEK": "スウェーデンクローナ",
    "NOK": "ノルウェークローネ",
    "DKK": "デンマーククローネ",
    "SGD": "シンガポールドル",
    "NZD": "ニュージーランドドル",
    "TRY": "トルコリラ",
    "AED": "アラブ首長国ディルハム",
    "SAR": "サウジリヤル",
    "EGP": "エジプトポンド"
}


@app.route('/', methods=['GET', 'POST'])
def index3():
    url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/JPY'# 円基準
    
    # 初期化
    result = None
    input_value = None
    selected_currency = None
    error_message = None

    rates = {} # API取得する為替レートの辞書

    # APIリクエストとエラーハンドリング
    try:
        response = requests.get(url)
        response.raise_for_status() # HTTPステータスコードを確認し、エラーなら例外を発生させる
        data = response.json() # JSONレスポンスを辞書に変換
        rates = data.get('conversion_rates', {}) # 為替レートの辞書
                    
    except requests.exceptions.RequestException as e:
        error_message = '為替レートを取得できません。時間をおいて再度お試しください。'
        rates = {} # エラー時は空の辞書にする
    
    # フォーム送信があった場合に計算を実行
    if request.method == 'POST':
        input_value = float(request.form['num']) # 入力は $0.99 も扱えるようint()ではなくfloat()
        selected_currency = request.form['operation']

        # 選択通貨 → 円 の換算レート
        rate = rates.get(selected_currency)
        if rate:
            # 「1円 = rate[通貨]」なので逆数にして円換算
            result = input_value / rate
            result = f"{int(result):,}" # 整数 + 3桁カンマ区切りにフォーマット

    # テンプレート用に (code, rate, name_ja) のリストを作る
    rates_display = []
    for code, name_ja in CURRENCY_NAMES_JA.items(): # {"USD": 1, "JPY": 147.5733, ...} のような辞書から取り出す
        rate = rates.get(code) # 為替レートを取得
        if rate: # rateがある場合のみ追加
            rates_display.append((code, rate, name_ja)) # 3つのタプルを追加したリストを作成

    return render_template(
        'index3.html',
        rates_display=rates_display, 
        result=result, 
        input_value=input_value, 
        selected_currency=selected_currency,
        error_message=error_message
    )

if __name__ == '__main__':
    app.run(debug=True)