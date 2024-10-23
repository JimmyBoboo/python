# Definerer en klasse som heter Bil
class Bil:
    # Initialiseringsmetode (konstruktør)
    def __init__(self, merke, modell, år):
        self.merke = merke
        self.modell = modell
        self.år = år

    # En metode for å skrive ut bilens detaljer
    def beskrivelse(self):
        return (f"Jeg har en {self.år} {self.merke} {self.modell}")

# Lager et objekt (en instans) av klassen Bil
min_bil = Bil("Toyota", "Corolla", 2020)

# Bruker metoden for å skrive ut detaljer om bilen
print(min_bil.beskrivelse())

