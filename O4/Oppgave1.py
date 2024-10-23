
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

print("------Filmer------")
print(film1)
print(film2)
print(film3)



    