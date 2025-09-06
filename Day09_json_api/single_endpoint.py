from flask import Flask, jsonify

app = Flask(__name__)

# シンプルなエンドポイントのAPI
@app.route('/api/endpoint', methods=['GET'])
def single_endpoint():
    # JSON形式で返す
    return jsonify({"message": "Response from single endpoint"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
