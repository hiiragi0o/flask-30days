# step4_delete.py
import sqlite3

conn = sqlite3.connect('favorites.db')
cursor = conn.cursor()

delete_id = input('削除するアイテムのIDを入力してください: ')

# delete_id は ? に代入されます
cursor.execute('DELETE FROM favorites WHERE id = ?', (delete_id,)) #　, があることで「1要素のタプル」になります 
print(f'ID {delete_id} を削除しました！')

conn.commit()
conn.close()