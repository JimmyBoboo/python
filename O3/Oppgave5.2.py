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
print("\n ****** A)*******")
# A Lag en funksjon som printer ut filmene.
for film in filmer:
    print(f"{film['name']} - {film['year']} has a rating of {film['rating']}.")

# B

def GjennomsnittRangering(filmer):
    
    total = 0
    for film in filmer:
        total = total + film['rating']
    
    return total / len(filmer)

print("\n ****** B)*******")
print(f"Gjennomsnitt rangeringen på alle filmene er {int(GjennomsnittRangering(filmer))}")

print("\n ****** C)*******")
# Lag en funksjon som tar en liste med filmer og årstall som parametere. 
def filmeretter2010 (filmer, year):
    tomliste = [] # Opprett en tom liste
    
    for film in filmer: #Opprettet en for løkke for å gå gjennonm listen. 
        if film['year'] >= year: # Gå gjennom listen, sjekke om 'year' er >=year (2010)
            tomliste.append(film) # Pushe inn til listen. Append.film
    return tomliste # Returner listen. 
        
filmer_2010 = filmeretter2010 (filmer, 2010) # Aktivere funksjonen, og legg in parametere. 2010 er 'year' i funksjonen. 
 
for film in filmer_2010:
    print(f"{film['name']} - {film['year']} has a rating of {film['rating']}.")
                    


    
    
    
    
 
  
    




 
    


            
