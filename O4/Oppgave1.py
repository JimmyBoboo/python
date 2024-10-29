# Oppgave a) 
# Har lagd en klasse som inneholder tittel, arstall og rating. 
# __in
class filmer:
    def __init__(self, tittel, arstall, rating):
        self.tittel = tittel
        self.arstall = arstall
        self.rating = rating

# objekter
film1 = filmer("Incpetion", 2010, 8.8)
film2 = filmer("The Martian", 2015, 8.0)
film3 = filmer("Joker", 2019, 8.4)

print("\n ------Filmer------")
print(f"{film1.tittel} - Utgivelsesår: {film1.arstall}, Score {film1.rating}")
print(f"{film2.tittel} - Utgivelsesår: {film2.arstall}, Score {film2.rating}")
print(f"{film3.tittel} - Utgivelsesår: {film3.arstall}, Score {film3.rating}")


# Oppgave b)
# I denne oppgaven returnerer den med string.
class filmer:
    def __init__(self, tittel, arstall, rating):
        self.tittel = tittel
        self.arstall = arstall
        self.rating = rating
    def __str__ (self):
        return (f"{self.tittel} - Utgivelsesår: {self.arstall}, score {self.rating}")
    
film1 = filmer("Incpetion", 2010, 8.8)
film2 = filmer("The Martian", 2015, 8.0)
film3 = filmer("Joker", 2019, 8.4)

print("\n ------Filmer, Returnert med string------")
print(film1)
print(film2)
print(film3)




    