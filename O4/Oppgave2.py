#Black jack
import random


class kortstokk:
    def __init__(self):
      logo = ("Hjerter", "Ruter", "Kløver", "Spar")
      rekker = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Knekt", "Dame", "Konge", "Ess")
      verdi = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Knekt": 10, "Dame": 10, "Konge": 10, "Ess": 11}

# Kortklassen
class kort:
    def __init__(self, logo, rekker):
        self.logo = logo
        self.rekker = rekker
        
        def __str__(self):
            return f'{self.rekker} av {self.logo}'

# Håndklassen

             
    
