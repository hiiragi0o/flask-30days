# SQLite データベース作成
import sqlite3

def init_db():
    conn = sqlite3.connect('vote.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS votes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            choice TEXT NOT NULL
        )
        ''')
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()