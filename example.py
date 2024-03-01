# date sort example 1
from datetime import datetime

# Beispiel-Datumsliste
daten = [
    datetime(2023, 5, 15),
    datetime(2024, 8, 21),
    datetime(2022, 12, 10),
    datetime(2023, 2, 28)
]

# Datumsliste sortieren
daten.sort()

# Formatierung und Ausgabe der sortierten Datumsliste
for datum in daten:
    formatiertes_datum = datum.strftime("%d.%m.%Y")  # Datum im gewünschten Format formatieren
    print(formatiertes_datum)
