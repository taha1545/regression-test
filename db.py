# 
import sqlite3

def init_db():
    conn = sqlite3.connect("weather.db")
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            temperature REAL,
            sunny INTEGER
        )
    """)

    # 
    cur.execute("SELECT COUNT(*) FROM weather")
    if cur.fetchone()[0] == 0:
        sample = [
            (10, 0),
            (14, 0),
            (18, 1),
            (20, 1),
            (22, 1),
            (25, 1),
            (30, 1),
            (5, 0),
            (7, 0)
        ]
        cur.executemany("INSERT INTO weather (temperature, sunny) VALUES (?, ?)", sample)
        conn.commit()

    conn.close()
