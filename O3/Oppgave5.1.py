# Opprett en liste med filmer, hvor hver film har en egen dictionary med dataene om en film. 
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

for film in filmer:
    print(f"{film['name']}, kom ut i {film['year']} og ratingen er {film['rating']}.")


    