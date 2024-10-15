filmer = [
    {'name': 'Inception', 'year': 2010, 'rating': 8.7},
    {'name': 'Inside Out', 'year': 2015, 'rating': 8.1},
    {'name': 'Con Air', 'year': 1997, 'rating': 6.9}
]

def filmer2010ogOppover (filmer, årstall):
    liste = []
    
    for film in filmer:
        if film['year'] >= årstall:
            liste.append(film)
            return liste

filmer_fra_2010 = filmer2010ogOppover(filmer, 2010)

for film in filmer_fra_2010:
    print(f"{film['name']} - {film['year']} has a rating of {film['rating']}.")
