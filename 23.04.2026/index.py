from openai import OpenAI
from dotenv import load_dotenv
import os
from pydantic import BaseModel, ConfigDict 

# .env-Datei laden
load_dotenv()

# Client initialisieren – OpenRouter als Base-URL
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)

antwort = """Vorname: Johann Wolfgang
Nachname: von Goethe"""

class Autor(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
    )

    vorname: str
    nachname: str


response = client.responses.parse(
    model="openai/gpt-oss-20b:free",
    input=[
        {
            "role": "system",
            "content": (
                "Extrahiere aus dem gegebenen Text genau den Autor. "
                "Gib ausschließlich strukturierte Daten zurück, passend zum Schema."
            ),
        },
        {
            "role": "user",
            "content": antwort,
        },
    ],
    text_format=Autor,
)

autor = response.output_parsed

print(autor.vorname)
print(autor.nachname)