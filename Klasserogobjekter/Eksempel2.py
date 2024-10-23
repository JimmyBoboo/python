class bil:
    def __init__(self, navn, årstall):
        self.navn = navn
        self.årstall = årstall
        
    def __str__(self):
        return (f"{self.navn} er fra {self.årstall}")
        
x = bil("Ferrari", 2012)
print(x)