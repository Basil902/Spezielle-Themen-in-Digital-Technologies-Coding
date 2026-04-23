import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()

conn = sqlite3.connect(os.getenv("DATABASE_FILE_PATH"))
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS llm_usage (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    model TEXT NOT NULL,
    usage_tokens INTEGER NOT NULL DEFAULT 0
);
""")

conn.commit()
conn.close()

# usage_tokens kann man über response.usage.total_tokens holen