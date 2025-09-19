# step2_insert.py
import sqlite3

conn = sqlite3.connect('favorites.db')
cursor = conn.cursor()

# 実行すると、ターミナルに入力欄が出ます
item = input('追加するアイテム名を入力してください: ')

cursor.execute('INSERT INTO favorites (name) VALUES (?)', (item,))
print(f'「{item}」を追加しました！')

conn.commit()
conn.close()