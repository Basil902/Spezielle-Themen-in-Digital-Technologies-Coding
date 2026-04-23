import re

antwort = """Vorname: Johann Wolfgang
Nachname: von Goethe"""

# Zeilen trennen
lines = antwort.splitlines()

vorname = None
nachname = None

for line in lines:
    v_match = re.search(r"Vorname:\s*(.+)", line)
    n_match = re.search(r"Nachname:\s*(.+)", line)
    
    if v_match:
        vorname = v_match.group(1)
    if n_match:
        nachname = n_match.group(1)

if vorname:
    print(vorname)

if nachname:
    print(nachname)