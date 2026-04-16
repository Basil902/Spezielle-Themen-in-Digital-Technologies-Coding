from openai import OpenAI
from dotenv import load_dotenv
import os
import sqlite3

# .env-Datei laden
load_dotenv()

db_file = os.getenv("DATABASE_FILE_NAME")

# Client initialisieren – OpenRouter als Base-URL
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)

# Messages-Liste aufbauen
# jede Antwort von der KI muss in der Liste hinzugefügt werden mit der role assistant, damit das LLM den Kontext kennt
# messages = [
#     {"role": "system",  "content": "Du bist ein hilfreicher Assistent."},
#     {"role": "user",    "content": "Wie viele Menschen leben in Köln?"},
#     {"role": "assistant", "content": "Etwa 1,07 Millionen Menschen leben in Köln - das macht sie zum viertgrößten und zweitökonomisch bedeutendsten Bundesland in Westfalen‑Rhein. Der exakte Einwohnerstand ändert sich ständig, daher gebe ich gern die aktuelle Zahl per 31. Dezember 2023 an: **1.068 481**."}
# ]

messages = [
    {
        'role': 'system',
        'content': 'Du bist ein hilfreicher Assitent und antwortest in knappen Sätzen und auf Englisch.'
    },
    {
        'role': 'assistant',
        'content': 'Hello, I\'m a chat assitant, how can I help you.'
    },
    {
        'role': 'user',
        'content': 'Hi, my name is Max.'
    },
    {
        'role': 'assistant',
        'content': 'Hello Max.'
    },
    {
        'role': 'user',
        'content': 'I am an Engineer.'
    },
    {
        'role': 'assistant',
        'content': 'Very good career choice.'
    },
    {
        'role': 'user',
        'content': 'What do I do for a living?'
    },
]

# Anfrage stellen
response = client.responses.create(
    model="openai/gpt-oss-20b:free",   # OSS-Modell bei OpenRouter
    input=messages,
)


    
usage = response.usage
usage_tokens = usage.total_tokens


def saveTokenToDB(token_usage)-> None:

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO llm_usage (model, usage_tokens)
    VALUES (?, ?)
    """, (
        "openai/gpt-oss-20b:free",
        token_usage
    ))

    conn.commit()
    conn.close()

# Antwort ausgeben
saveTokenToDB(usage_tokens)
print(response.output_text)
