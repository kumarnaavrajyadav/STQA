import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "testforge.db")

def save_test_results(results):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS test_results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        total INTEGER,
        passed INTEGER,
        failed INTEGER,
        pass_rate TEXT
    )
    """)

    summary = results.get("summary", {})
    cursor.execute("""
        INSERT INTO test_results (date, total, passed, failed, pass_rate)
        VALUES (?, ?, ?, ?, ?)
    """, (datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
          summary.get("total"),
          summary.get("passed"),
          summary.get("failed"),
          summary.get("pass_rate")))

    conn.commit()
    conn.close()
