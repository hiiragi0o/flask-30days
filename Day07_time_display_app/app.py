from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    # 現在時刻
    now = datetime.now()
    # 見やすいフォーマットに変換（例: 2025-09-04 10:30:15）
    current_time = now.strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', current_time=current_time)


if __name__ == '__main__':
    app.run(debug=True)