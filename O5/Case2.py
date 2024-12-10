# -----------------------Oppgave 1---------------------------------------------
# Implementer funksjonen print_car_information() som printer ut informasjon om en bil på følgende format:
# Brand: Toyota # Model: Corolla # Price. 96000,- # Manufactured: 2012-8 # Condition: Used
def print_car_information(brand, model, price, year, month, Condition):
    print(f"Brand: {brand}")
    print(f"Model: {model}")
    print(f"Price: {price}")
    print(f"Manufactured: {year} - {month}")
    print(f"Condition: {Condition}")
    
# -----------------------Oppgave 2---------------------------------------------
# Implementer funksjonen create_car() som tar forskjellig informasjon om en bil som parametere. 
# Denne skal lage en dictionary for en bil med korrekte nøkkelverdier slik som beskrevet i Case-beskrivelsen, 
# legger den inn i registeret og returner til slutt bil-dictionaryen.
def create_car(car_register, brand, model, price, year, month, new, km):
    car_register[brand + model] = {
        "brand": brand,
        "Model": model,
        "Price": price,
        "year": year,
        "Month": month,
        "New": new,
        "km": km
    }
    return car_register
# -----------------------Oppgave 3---------------------------------------------
# Implementer funksjonen get_car_age() som returnerer bilens alder fra inneværende år.
# F.eks. Hvis bilen er fra 2019, og inneværende år er 2022, er bilen 3 år (vi bryr oss ikke om måned).
from datetime import datetime
def get_car_age(year_lagd):
    naa_dagens_aar = datetime.now().year
    car_age = naa_dagens_aar - year_lagd
    return car_age

# -----------------------Oppgave 4---------------------------------------------
# Implementer funksjonen rent_car_monthly_price() som returner månedsprisen for å leie en bil (prisen skal være avrundet til 2 desimaler). 
# Den årlige prisen er 40% av totalprisen av bilen. Hvis bilen er ny, skal det også legges til en påslag på 1000kr i måneden.
def rent_car_monthly(bilpris, hvis_ny):
    arlig_pris = 0.4 * bilpris
    manedlig_pris = arlig_pris / 12
    if hvis_ny:
        manedlig_pris += 1000
        return round(manedlig_pris, 2)
    
# -----------------------Oppgave 5---------------------------------------------
# Implementer funksjonen next_eu_control() som returnerer et dato-objekt for neste EU-kontroll. 
# EU-kontrollen skal skje hver 2. år, fra året og måneden bilen ble produsert. Det er OK om man setter den 1. i måneden i dato-objektet man returnerer.
from datetime import date
def next_eu_control(year_lagd, maned_lagd):
    naa_dagens_dato = date.today()
    naa_dagens_aar = naa_dagens_dato.year
    naa_dagens_maned = naa_dagens_dato.month
    
    year_differanse = (naa_dagens_aar - year_lagd) // 2
    sist_EU_kontroll = year_lagd + (year_differanse * 2)
    
    if (naa_dagens_aar > sist_EU_kontroll or (naa_dagens_aar == sist_EU_kontroll and naa_dagens_maned >= maned_lagd)):
        neste_EU_sjekk = sist_EU_kontroll + 2
    
    else:
        neste_EU_sjekk = sist_EU_kontroll

    return date(neste_EU_sjekk, maned_lagd, 1)

# -----------------------Oppgave 6---------------------------------------------
from datetime import datetime

def calculate_total_price(base_pris, year_lagd, hvis_ny):
    naa_dagens_aar = datetime.now().year
    
    avgift_tabell_på_bil = [
        {"minste_alder": 0, "maks_alder": 3, "avgift": 6681},
        {"minste_alder": 4, "maks_alder": 11, "avgift": 4034},
        {"minste_alder": 12, "maks_alder": 29, "avgift": 1729},
        {"minste_alder": 30, "maks_alder": float("inf"), "avgift": 0}
    ]
    
    if hvis_ny:
        avgift = 10783
    else:
        age = naa_dagens_aar - year_lagd
        
        for avgift_bil in avgift_tabell_på_bil:
            if avgift_bil["minste_alder"] <= age <= avgift_bil ["maks_alder"]:
                avgift = avgift_bil["avgift"]
                break
            
    total_pris = base_pris + avgift
    return total_pris

# -----------------------Oppgave 7---------------------------------------------
class car:
    def __init__(self, brand, model, price, year, month, new, km):
        self.brand = brand
        self.model = model
        self.price = price
        self.year = year
        self.month = month
        self.new = new
        self.km = km
        
    
    def print_car_information(self):
        pass

    def get_car_age(self):
        pass

    def next_eu_control(self):
        pass

    def rent_car_monthly_price(self):
        pass

    def calculate_total_price(self):
        pass

    def is_new(self):
        pass
    
# Grunnen til at jeg ikke tok med create_car er fordi, det er ikke nødvendig å ha en metode for å lage en bil, når jeg allerede har en klasse som gjør det. 
