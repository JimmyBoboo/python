
class bil:
    def __init__(self, navn, årstall):
        self.navn = navn
        self.årstall = årstall
        
x = bil("Ferrari", 2012)

print(f"{x.navn}, fra {x.årstall} er drømmebilen")