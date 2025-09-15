import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
from newsapi import NewsApiClient # requests の代わりに newsapi 公式ライブラリを使う

load_dotenv()
API_KEY = os.getenv('API_KEY')

app = Flask(__name__)
newsapi = NewsApiClient(api_key=API_KEY) # NewsApiClient のインスタンスを作成

# helper関数：全ニュースソースとドメインを取得して、カンマ区切りで渡す
def get_source_and_domains():
    all_sources = newsapi.get_sources()['sources']
    sources = []
    domains = []
    for e in all_sources:
        id = e['id']
        # URLからドメイン名だけを抽出
        domain = e['url'].replace("http://","").replace("https://", "").replace("www.", "")
        slash = domain.find('/')
        if slash != -1:
            domain = domain[:slash] # 最初の/までを抽出
            sources.append(id) # ニュースソースIDを追加
            domains.append(domain) # ドメイン名を追加
    
    # 'cnn,bbc-news,the-wall-street-journal'のような単一の文字列を作成
    # 'cnn.com,bbc.com,wsj.com'のような文字列を作成
    return ','.join(sources), ','.join(domains)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        keyword = request.form['keyword']

        # 全ソースとドメインを取得
        sources, domains = get_source_and_domains()

        # totalResultsを確認する目的で、キーワードで関連ニュースを取得
        # デフォルトのページサイズ 20件で応答し、totalResultsを返している
        related_news = newsapi.get_everything(
            q=keyword,
            sources=sources,
            domains=domains,
            language='en',
            sort_by='relevancy'
        )

        # 記事数の上限を100に設定
        no_of_articles = min(related_news['totalResults'], 100)

        # 実際のニュース記事を取得
        all_articles = newsapi.get_everything(
            q=keyword,
            sources=sources,
            domains=domains,
            language='en',
            sort_by='relevancy',
            page_size=no_of_articles # 取得する記事数を指定(100件まで)
        )['articles']
        return render_template('index.html', all_articles=all_articles, keyword=keyword)

    else:
        # GETアクセス時はトップヘッドラインを表示
        top_headlines =  newsapi.get_top_headlines(language='en',country='us')
        total_results = min(top_headlines['totalResults'], 100)
        all_headlines = newsapi.get_top_headlines(
                        language='en',
                        page_size=total_results
        )['articles']
        return render_template('index.html', all_articles=all_headlines)

if __name__ == '__main__':
    app.run(debug=True)