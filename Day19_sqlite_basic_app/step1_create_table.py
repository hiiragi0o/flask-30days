# step1_create_table.py
import sqlite3

# データベースに接続（ファイルがなければ作成される）
conn = sqlite3.connect('favorites.db')
cursor = conn.cursor() # カーソルを作成

# favorites というテーブルを作成
cursor.execute('''
    CREATE TABLE IF NOT EXISTS favorites (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
''')

print('テーブルを作成しました！')

conn.commit()
conn.close()