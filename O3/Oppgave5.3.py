print("\n --------Oppgave 5.3 A) ---------")
def skrive_til_fil(filmer, filnavn):
    with open(filnavn, "w") as f:
        for film in filmer:
            liste = (f"\n {film['name']} - {film['year']} has a rating of {film['rating']}.")
            f.write(liste)
    print(f"filmen er skrevet til {filnavn}")
        
filnavn = "movies.txt"
       
filmer = [
    {'name': 'Inception', 'year': 2010, 'rating': 8.7},
    {'name': 'Inside Out', 'year': 2015, 'rating': 8.1},
    {'name': 'Con Air', 'year': 1997, 'rating': 6.9}
]

# Starte funksjonen for å sette inn lista i filen "Movies"
skrive_til_fil(filmer, filnavn)

# En variabel som er linket til Filen "movies.txt".
filnavn = "movies.txt"  
print("\n --------Oppgave 5.3 B---------") 

def leseFilnavn(filnavn):
    with open (filnavn, "r") as f:
        liste_i_filen = f.read()
        print(f"Innholdet i listen er: {filnavn}")
        print (liste_i_filen)
    if liste_i_filen == FileNotFoundError:
        print (f"{filnavn} er ikke funnet.")
        
# Starte funksjonen til å lese innholdet i filen, og bli sendt til terminalen.
leseFilnavn(filnavn)

