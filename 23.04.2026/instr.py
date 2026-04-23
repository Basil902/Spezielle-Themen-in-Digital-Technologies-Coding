import os
import instructor
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel, ConfigDict

load_dotenv()

openai_client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)

# API Key sicher über Umgebungsvariable laden
client = client = instructor.from_openai(openai_client)

antwort = """Vorname: Johann Wolfgang
Nachname: von Goethe"""


class Autor(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
    )

    vorname: str
    nachname: str


autor = client.chat.completions.create(
    model="openai/gpt-oss-20b:free",
    response_model=Autor,
    messages=[
        {
            "role": "system",
            "content": "Extrahiere Vorname und Nachname strukturiert aus dem Text.",
        },
        {
            "role": "user",
            "content": antwort,
        },
    ],
)

print(autor.vorname)
print(autor.nachname)