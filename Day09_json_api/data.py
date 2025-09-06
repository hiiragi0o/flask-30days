from flask import Flask, Response, json

app = Flask(__name__)

# 日本語を返すAPI
@app.route('/api/data', methods=['GET'])
def data():
    # 固定データ
    data = {
        "type": "飲み物",
        "temperature": "アイス",
        "menu_items": ["チョコレート ムース ラテ", "ビター クリーム コーヒー", "ほうじ茶フラペチーノ"]
    }
    # json.dumps を使い、Flask の Response で返す
    json_str = json.dumps(data, ensure_ascii=False) # ensure_ascii=False で日本語をそのまま出力
    return Response(json_str, content_type='application/json; charset=utf-8')

if __name__ == '__main__':
    app.run(debug=True)