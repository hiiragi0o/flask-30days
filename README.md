# Flask 30日チャレンジ
URL
 https://*****.com デプロイは未定<br >

<br><br>
## 概要

これは **Flask 30日チャレンジ** の成果物をまとめたものです。<br>
「1日1アプリ＝必ず完成させる」を目標に、30日間で小さなWebアプリを作り続けました。<br>
シンプルでも動くものを完成させることを重視し、Flaskの基礎からAPI連携・DB活用・簡易ゲームまで、幅広く習得しました。



## 使用技術

* **バックエンド**: Python 3.11.7 / Flask 3.1.2
* **フロントエンド**: HTML, CSS (Bootstrap含む), JavaScript
* **データベース**: SQLite
* **外部API**: OpenWeather, NewsAPI, GitHub API, Google Books API など
* **その他**: JSON, CSV, Pillow(画像処理), Markdown, qrcode, （本番環境デプロイ）

* **作業環境**: macOS Sequoia 15.6.1

## ディレクトリ構成

```
Flask30Days/
│
├── Day01_omikuji_app/
├── Day02_todo_app/
├── Day03_quote_app/
...
```


## 学んだこと

* Flaskを使った **Webアプリ開発の基本フロー**
* 外部API連携やSQLiteを使った **データ処理**
* HTML/CSS/JavaScriptを組み合わせた **フロント実装力**
* 30日間での **継続的な学習と成果物の完成**




## Flask を選んだ理由

  * 「ルーティング」「リクエスト/レスポンス」など、Web開発の基本をしっかり経験できる。
  * Flaskは実務でもAPI開発や小規模サービスで使われる。
  * Django より軽量。(Django は学習済み)
  * 毎日「完成」が実現しやすい。
<br>


<br><br>


# Flask 30日チャレンジリスト

### Day 1〜10（基礎・習慣化）

1. おみくじアプリ
2. TODOリスト（追加のみ）
3. ランダム名言表示
4. 数字カウンター
5. 計算機（四則演算）
6. テキスト反転アプリ
7. 現在時刻表示
8. 画像アップロード → 表示
9. JSONを返すAPI
10. Markdownプレビューア

---

### Day 11〜20（外部API & DB）

11. 天気情報アプリ（OpenWeather）
12. 為替レート表示（外部API）
13. ニュース一覧（NewsAPI）
14. GitHubユーザー情報表示
15. 書籍検索（Google Books API）
16. TODOリスト（SQLite保存）
17. 掲示板（SQLite）
18. 短縮URLサービス
19. お気に入りリスト（削除可）
20. 投票アプリ

---

### Day 21〜30（便利ツール & 簡易ゲーム）

21. QRコード生成
22. CSVアップロード → 表示
23. 画像リサイズ
24. 文字数カウント
25. 正規表現チェッカー
26. クイズアプリ（選択式）
27. じゃんけんアプリ（vs CPU）
28. オセロ風（簡易版・マス目＋石設置のみ）
29. シューティング風（ボタンで敵を倒す演出）
30. **「30日アプリまとめ」サイト（全作品のリンク集）**
31. ポモドーロタイマーのアプリ


<br><br>

# アプリごとのまとめ

### Day01 - おみくじアプリ

画面更新するとランダムに結果を表示。 <br>
使用技術：Flask（ルーティング / テンプレート）, HTML, CSS, randomモジュール


<img width="800" alt="スクリーンショット 2025-08-30 13 04 24" src="https://github.com/user-attachments/assets/73ab4c38-496c-4526-9b84-946299830300" />

---

### Day02 - TODOアプリ

タスクを入力してリストに追加。未完了タスク　→ クリックで非表示。 <br>
使用技術：Flask（ルーティング / テンプレート）, HTML, CSS

<img width="800" alt="スクリーンショット 2025-08-30 15 20 22" src="https://github.com/user-attachments/assets/08096e11-f73f-49f3-b59f-d4de81f1f5a0" />


---

### Day03 - ランダム名言表示

ボタンクリックで、ランダムに1つ名言・画像を表示。 <br>
使用技術：Flask（ルーティング / テンプレート）, HTML, CSS, randomモジュール

<img width="800" alt="スクリーンショット 2025-08-31 16 16 40" src="https://github.com/user-attachments/assets/efa84954-73aa-4c0e-9138-a96bf5e1a124" />


<img width="800" alt="スクリーンショット 2025-08-31 16 18 03" src="https://github.com/user-attachments/assets/c8f48adc-249b-4677-b194-e106d99e13c5" />


---

### Day04 - 数字カウンター

カウントアップ・ダウンが可能なシンプルカウンター。 <br>
使用技術：Flask（ルーティング / セッション管理 / 環境変数）, HTML <br>
学習のポイント：「リクエストが終わったら情報が消える」Flaskの基本性質を理解する。状態を維持するにはセッションが必要。環境変数を扱い、セキュリティを意識。


---

### Day05 - 計算機アプリ

四則演算（+ - × ÷）に対応。ゼロで割り算した場合に徐算エラーを表示。 <br>
使用技術：Flask（フォーム送信処理）, HTML, CSS, JavaScript（非同期通信）
学習のポイント：
- ウェブフォームから送信されたデータをPythonのFlaskで受け取り、演算処理を行った結果を表示する。
- 非同期通信（JavaScriptのfetch）を導入し、ページ全体をリロードせずに計算結果を動的に更新できる点を学ぶ。



---

### Day06 - テキスト反転アプリ

入力文字を逆順に変換して表示。 <br>
使用技術：Flask（フォームデータ受け取り）, HTML, CSS
学習のポイント：Flaskでフォームからデータを受け取って処理し、結果を返す最小のサイクルを学ぶ。文字列の反転 [::-1] の使い方。これまでのコードを使い組み立てる。


---

### Day07 - 現在時刻表示

アクセス時点のサーバー時刻を表示。 <br>
使用技術：Flask（ルーティング）, datetimeモジュール, HTML, CSS
学習のポイント：
- datetime モジュールを使って「現在時刻」を取得する。
- flask-moment（Flaskの拡張機能）を使って JavaScript の moment.js ライブラリを扱う
- pytz（Pythonでタイムゾーンを扱うためのライブラリ）を使って、世界中のタイムゾーン情報を取得

---

### Day08 - 画像アップロード表示

画像をアップロードしてブラウザに表示。 <br>
使用技術：Flask（ファイルアップロード処理 / request.files）, HTML

---

### Day09 - JSON API

固定データをJSON形式で返すAPI。 <br>
使用技術：Flask（`jsonify` / APIエンドポイント作成）

---

### Day10 - Markdownプレビュー

入力MarkdownをHTMLに変換して表示。 <br>
使用技術：Flask（フォーム送信処理）, markdownライブラリ, HTML

---

### Day11 - 天気情報表示

OpenWeather APIを利用して都市の天気を取得。 <br>
使用技術：Flask（外部APIとの通信）, requestsライブラリ, HTML

---

### Day12 - 為替レート換算

外部APIで為替レートを取得し換算。 <br>
使用技術：Flask（外部API利用）, requestsライブラリ, HTML

---

### Day13 - ニュース一覧表示

NewsAPIから最新ニュースを取得。 <br>
使用技術：Flask（外部API利用）, requestsライブラリ, HTML, CSS

---

### Day14 - GitHubユーザー情報表示

ユーザー名からGitHub APIを呼び出し、プロフィールを表示。 <br>
使用技術：Flask（外部API利用）, requestsライブラリ, HTML

---

### Day15 - 書籍検索アプリ

Google Books APIを利用して書籍情報を表示。 <br>
使用技術：Flask（外部API利用）, requestsライブラリ, HTML, CSS

---

### Day16 - TODOアプリ（SQLite保存）

SQLiteを利用しタスクを保存。 <br>
使用技術：Flask（SQLAlchemy / DB接続）, SQLite, HTML, CSS

---

### Day17 - 掲示板アプリ

投稿内容をDBに保存して表示。 <br>
使用技術：Flask（SQLAlchemy / DB操作）, SQLite, HTML, CSS

---

### Day18 - URL短縮サービス

入力されたURLを短縮し保存。 <br>
使用技術：Flask（ルーティング / DB操作）, SQLite, HTML

---

### Day19 - お気に入りリスト（追加・削除）

アイテムの追加と削除が可能。 <br>
使用技術：Flask（CRUD処理）, SQLite, HTML, CSS

---

### Day20 - 投票アプリ

投票結果を集計して表示。 <br>
使用技術：Flask（DB集計処理）, SQLite, HTML, CSS

---

### Day21 - QRコード生成

入力文字からQRコードを生成。 <br>
使用技術：Flask（ファイル生成 / レスポンス返却）, qrcodeライブラリ, HTML

---

### Day22 - CSVアップロード表示

CSVファイルを読み込み、テーブル表示。 <br>
使用技術：Flask（ファイルアップロード）, pandas, HTML, CSS

---

### Day23 - 画像リサイズ

画像を指定サイズに変換して表示。 <br>
使用技術：Flask（ファイル処理）, Pillowライブラリ, HTML

---

### Day24 - 文字数カウント

入力テキストの文字数をカウント。 <br>
使用技術：Flask（フォーム処理）, HTML

---

### Day25 - 正規表現チェッカー

正規表現パターンで文字列をテスト。 <br>
使用技術：Flask（フォーム処理）, reモジュール, HTML

---

### Day26 - クイズアプリ

選択式クイズを出題し正答判定。 <br>
使用技術：Flask（DB利用 / フォーム処理）, SQLite, HTML, CSS

---

### Day27 - じゃんけんアプリ

ユーザーとCPUでじゃんけん対戦。 <br>
使用技術：Flask（ルーティング）, HTML, JavaScript（フロント判定）

---

### Day28 - オセロ風（簡易版）

石を置けるシンプルなオセロ盤。 <br>
使用技術：Flask（ルーティング）, HTML, JavaScript（盤面操作）

---

### Day29 - シューティング風

簡易的なシューティングゲーム。 <br>
使用技術：Flask（ルーティング）, HTML, JavaScript（ゲーム処理）

---

### Day30 - まとめサイト

全30日のアプリ一覧ページ。 <br>
使用技術：Flask（ルーティング / テンプレート）, HTML, CSS

---

### Day31 - ポモドーロタイマー

作業効率化用のタイマーアプリ。 <br>
使用技術：Flask（ルーティング）, HTML, CSS, JavaScript（タイマー処理）


