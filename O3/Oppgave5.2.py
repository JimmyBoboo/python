# Liste med filmer, hvor hver film er i en egen dictionary.
filmer = [
    {'name': 'Inception', 'year': 2010, 'rating': 8.7},
    {'name': 'Inside Out', 'year': 2015, 'rating': 8.1},
    {'name': 'Con Air', 'year': 1997, 'rating': 6.9}
]

def leggTilFilm(filmer, name, year, rating=5.0):
    filmer.append({'name': name, 'year': year, 'rating': rating})

leggTilFilm(filmer, 'The martian', 2015, 8.9)
leggTilFilm(filmer, 'Notebook', 2004, 8.3)
leggTilFilm(filmer, 'Gemini man', 2019, )

# A Lag en funksjon som printer ut filmene.
for film in filmer:
    print(f"{film['name']} - {film['year']} has a rating of {film['rating']}.")

# B

def GjennomsnittRangering(filmer):
    
    total = 0
    for film in filmer:
        total = total + film['rating']
    
    return total / len(filmer)

print(f"Gjennomsnitt rangeringen på alle filmene er {int(GjennomsnittRangering(filmer))}")

    
