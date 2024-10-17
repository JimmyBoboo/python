def skrive_til_fil(filmer, filnavn):
    with open(filnavn, "w") as f:
        for film in filmer:
            liste = (f"\n {film['name']} - {film['year']} has a rating of {film['rating']}.")
            f.write(liste)
            print(f"filmen er skrevet til {filnavn}")
        
        
filmer = [
    {'name': 'Inception', 'year': 2010, 'rating': 8.7},
    {'name': 'Inside Out', 'year': 2015, 'rating': 8.1},
    {'name': 'Con Air', 'year': 1997, 'rating': 6.9}
]

# Filnavn "movies.txt"
filnavn = "movies.txt"  
  



# Starte funksjonen for å sette inn lista i filen "Movies"
skrive_til_fil(filmer, filnavn)

# Starte funksjonen til å lese innholdet i filen, og bli sendt til terminalen.


