# Funksjon for å skrive filmer til en fil
def skriv_filmer_til_fil(filmer, filnavn):
    with open(filnavn, 'w') as f:
        for film in filmer:
            linje = f"{film['tittel']} - {film['år']} has a rating of {film['rating']}\n"
            f.write(linje)
    print(f"Filmen(e) er skrevet til {filnavn}")

# Funksjon for å lese fra fil og skrive ut til terminalen

filmer = [
    {"tittel": "The Lion King", "år": 1994, "rating": 8.5},
    {"tittel": "Inception", "år": 2010, "rating": 8.8},
    {"tittel": "The Matrix", "år": 1999, "rating": 8.7}
]

# Filnavn
filnavn = "movies.txt"

# Skriv filmene til filen
skriv_filmer_til_fil(filmer, filnavn)


