import sqlite3
import json

class DB:
    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def create_tables(self):
        self.cursor.execute("""
                        CREATE TABLE IF NOT EXISTS stocks (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        symbol TEXT NOT NULL,
                        data TEXT,
                        timestamp TEXT
                        )
                    """)
        self.connection.commit()

    def save_stock(self, symbol, data):
        json_data = json.dumps(data)
        self.cursor.execute("""
                            INSERT INTO stocks (symbol, data, timestamp)
                            VALUES (?, ?, datetime('now'))
                            """, (symbol, json_data))
        self.connection.commit()

    def get_stocks(self):
        self.cursor.execute("SELECT symbol, data, timestamp FROM stocks")
        rows = self.cursor.fetchall()
        return rows
    
