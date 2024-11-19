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

pris_på_ny_bil = calculate_total_price(300000, 2024, True)
print(f"Total prisen nye bilen er: {pris_på_ny_bil} kr")
pris_på_ny_bil = calculate_total_price(150000, 2015, False)
print(f"Total prisen på brukte bilen er: {pris_på_ny_bil} kr")