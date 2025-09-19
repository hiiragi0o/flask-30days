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

def update_item():
    update_id = input('更新するID: ')
    new_name = input('新しい名前: ')

    conn = sqlite3.connect('favorites.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE favorites SET name = ? WHERE id = ?', (new_name, update_id,))
    conn.commit()
    conn.close()
    print(f'ID{update_id} を 「{new_name}」 に更新しました！')

def search_items():
    keyword = input('検索ワード: ')

    conn = sqlite3.connect('favorites.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name FROM favorites WHERE name LIKE ?', ('%' + keyword + '%',))
    rows = cursor.fetchall()
    conn.close()

    print('--- 検索結果 ---')
    for row in rows:
        print(f'[{row[0]}] {row[1]}')

# メインの処理
def main():
    init_db()
    while True:
        print('\n--- お気に入りリスト ---')
        print('1. 追加')
        print('2. 一覧表示')
        print('3. 削除')
        print('4. 更新')
        print('5. 検索')
        print('6. 終了')
        choice = input('選択: ')

        if choice =='1':
            add_item()
        elif choice =='2':
            show_items()
        elif choice == '3':
            delete_item()
        elif choice == '4':
            update_item()
        elif choice == '5':
            search_items()
        elif choice =='6':
            break
        else:
            print('無効な入力です')

# 自作の main() 関数を呼び出す。サーバー起動はしない。
if __name__ == '__main__':
    main()