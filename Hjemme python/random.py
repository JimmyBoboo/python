# Modifisert funksjon som setter default-rating til 5.0
def legg_til_film(filmliste, name, year, rating=5.0):
    film = {
        "name": name,
        "year": year,
        "rating": rating
    }
    filmliste.append(film)

# Opprett en tom filmliste
filmer = []

# Legger til tre filmer, hvorav én uten rating
legg_til_film(filmer, "Inception", 2010, 8.8)
legg_til_film(filmer, "The Matrix", 1999, 8.7)
legg_til_film(filmer, "The Grand Budapest Hotel", 2014)  # Ingen rating spesifisert

# Skriv ut filmlisten for å verifisere at default-rating fungerer
print(filmer)
