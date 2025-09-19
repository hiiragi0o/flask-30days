# step3_select.py
import sqlite3

conn = sqlite3.connect('favorites.db')
cursor = conn.cursor()

cursor.execute('SELECT id, name FROM favorites')
rows = cursor.fetchall()

print('--- お気に入り一覧 ---')
for row in rows:
    print(f'[{row[0]}] {row[1]}')

    conn.close()