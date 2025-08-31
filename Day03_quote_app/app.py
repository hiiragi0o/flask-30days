import os
import random

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

# 名言と作者名のリスト
quotes = [
    {'quote': '誰かの為に生きてこそ、人生には価値がある', 'author': 'ドイツ・物理学者　アインシュタイン'},
    {'quote': 'たぶん失敗するだろうと思ったけど、重要な事だからやることにした', 'author': 'アメリカ・実業家　イーロン・マスク'},
    {'quote': '腰をすえて座り一日中読むことが賢明さを得る最もよい方法である', 'author': 'アメリカ・投資家　ウォーレン・バフェット'},
    {'quote': 'それでも地球は動いている', 'author': 'イタリア・物理学者、天文学者　ガリレオ・ガリレイ'},
    {'quote': '感情や直感、望みに従い、ハッピーになれることをしなさい', 'author': 'オランダ・デザイナー、絵本作家　ディック・ブルーナ'},
    {'quote': '人を非難するのは、ちょうど天に向かってつばをするようなもので、 必ず我が身に返ってくる', 'author': 'アメリカ・講師　デール・カーネギー'},
    {'quote': '幸せを祈る気持ちだけでは、平和を成すことはできない。', 'author': 'スウェーデン・発明家　ノーベル'},
    {'quote': '万物は数なり', 'author': '古代ギリシア・数学者、哲学者　ピタゴラス'},
    {'quote': '私達の財産、それは私達の頭の中にある', 'author': 'オーストリア・音楽家　モーツァルト'},
    {'quote': 'リスクを取る勇気がなければ、何も達成することがない人生になる', 'author': 'アメリカ・ボクサー　モハメド・アリ'},
    {'quote': '人間はやり通す力があるかないかによってのみ、称賛または非難に値する。', 'author': 'イタリア・芸術家　レオナルド・ダ・ヴィンチ'},
    {'quote': '千里の道も一歩から', 'author': '中国・思想家　老子'},
    {'quote': '実に単純なことです。ひとはひとをよろこばせることが一番うれしい', 'author': '日本・絵本作家　やなせたかし'}
    ]

# 名言と著者のリストからランダムに選んで表示
def random_quote():
    return random.choice(quotes)

# 画像をランダムに選んで表示
def random_image():
    img_dir = './static/'
    img_list = os.listdir(img_dir)
    return random.choice(img_list)


@app.route('/')
def index():
    quote_data = random_quote()
    image = random_image()
    return render_template('index.html', **quote_data, random_image=image)

@app.route('/add', methods=['GET', 'POST'])
def add():
    # フォームのmethodがPOSTだった場合、フォームの各要素を取得しquotesリストに追加
    if request.method =='POST':
        quote = request.form['quote']
        author = request.form['author']

        # それぞれの値をリストで保持
        quotes.append({'quote': quote, 'author': author})
        return redirect(url_for('add'))
    
    # GETの場合、追加された名言を表示すsるためにquotesリストをテンプレートに渡す
    return render_template('add.html', quotes=quotes)


if __name__ == '__main__':
    app.run()
