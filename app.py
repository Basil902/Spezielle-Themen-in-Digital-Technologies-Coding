import streamlit as st
import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

db_file = os.getenv("DATABASE_FILE_NAME")

st.title("📊 LLM Token Usage")

# Verbindung zur DB
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Daten holen
cursor.execute("SELECT * FROM llm_usage")
rows = cursor.fetchall()

# Spaltennamen holen
column_names = [description[0] for description in cursor.description]

conn.close()

# Tabelle anzeigen
if rows:
    st.subheader("Usage Data")

    # Header anzeigen
    st.write(" | ".join(column_names))
    st.write("---" * len(column_names))

    # Zeilen anzeigen
    for row in rows:
        st.write(" | ".join(str(cell) for cell in row))
else:
    st.write("No data found.")