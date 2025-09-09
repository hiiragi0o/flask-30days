# （外部API）ExchangeRate-APIでAPI取得してhtmlで表示
# ドル円の為替レートを表示
import os
from flask import Flask, jsonify, render_template
from flask.cli import load_dotenv
import requests

load_dotenv()
API_KEY = os.getenv('API_KEY')

app = Flask(__name__)

@app.route('/')
def index2():
    url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD'
    
    output_jpy = None # 初期化
    rates = {}

    try:
        response = requests.get(url)
        response.raise_for_status() # HTTPステータスコードを確認し、エラーなら例外を発生させる

        data = response.json() # JSONレスポンスを辞書に変換
        rates = data.get('conversion_rates', {}) # 為替レートの辞書
        
        jpy_rate = rates.get("JPY") # JPYの為替レートを取得
        if jpy_rate is not None:
            input_usd = 1 # 1USDとする
            output_jpy = int(input_usd * jpy_rate) # 整数化
            # 💡 このprint文はターミナルに出力されます
            print(f"1 USD = {output_jpy} JPY") # デバッグ用 ターミナルに表示
        else:
            print("エラー: JPYの為替レートが見つかりませんでした。")
            
    except requests.exceptions.RequestException as e:
        print(f"APIリクエストエラー: {e}")
        
    return render_template('index2.html', rates=rates, jpy_rate=jpy_rate, input_usd=input_usd, output_jpy=output_jpy)

if __name__ == '__main__':
    app.run(debug=True)