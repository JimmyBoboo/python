# -----------------------Oppgave 1---------------------------------------------
def print_car_information(brand, model, price, year, month, Condition):
    print(f"Brand: {brand}")
    print(f"Model: {model}")
    print(f"Price: {price}")
    print(f"Manufactured: {year} - {month}")
    print(f"Condition: {Condition}")
    
# -----------------------Oppgave 2---------------------------------------------
def create_car(car_register, brand, model, price, year, month, new, km):
    car_register = {
        "brand": brand,
        "Model": model,
        "Price": price,
        "year": year,
        "Month": month,
        "New": new,
        "km": km
    }

# -----------------------Oppgave 3---------------------------------------------
from datetime import datetime
def get_car_age(year_lagd):
    naa_dagens_aar = datetime.now().year
    car_age = naa_dagens_aar - year_lagd
    return car_age

# -----------------------Oppgave 4---------------------------------------------
def rent_car_monthly(bilpris, hvis_ny):
    arlig_pris = 0.4 * bilpris
    manedlig_pris = arlig_pris / 12
    if hvis_ny:
        manedlig_pris += 1000
        return round(manedlig_pris, 2)
    
# -----------------------Oppgave 5---------------------------------------------
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

