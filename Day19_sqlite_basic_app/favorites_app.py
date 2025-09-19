# step5「テーブル作成／追加／表示／削除」をまとめた小さなコンソールアプリ
import sqlite3

def init_db():
    conn = sqlite3.connect('favorites.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS favorites (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    ''')

    conn.commit()
    conn.close()

def add_item():
    item = input('追加するアイテム名: ')
    conn = sqlite3.connect('favorites.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO favorites (name) VALUES (?)', (item,))
    conn.commit()
    conn.close()
    print(f'「{item}」を追加しました！')

def show_items():
    conn = sqlite3.connect('favorites.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name FROM favorites')
    rows = cursor.fetchall()
    conn.close()

    print('--- お気に入り一覧 ---')
    for row in rows:
        print(f'[{row[0]}] {row[1]}')

def delete_item():
    delete_id = input('削除するID: ')
    conn = sqlite3.connect('favorites.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM favorites WHERE id = ?', (delete_id,))
    conn.commit()
    conn.close()

    print(f'ID {delete_id} を削除しました！')

def main():
    init_db()
    while True:
        print('\n--- お気に入りリスト ---')
        print('1. 追加')
        print('2. 一覧表示')
        print('3. 削除')
        print('4. 終了')
        choice = input('選択: ')

        if choice =='1':
            add_item()
        elif choice =='2':
            show_items()
        elif choice == '3':
            delete_item()
        elif choice =='4':
            break
        else:
            print('無効な入力です')

# 自作の main() 関数を呼び出す。サーバー起動はしない。
if __name__ == '__main__':
    main()