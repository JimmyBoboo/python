def calculate_average_ware_rating(ware):
    rating = ware.get("rating", [])
    
    if not rating: #Dette er for å se om listen er tom.
        return None
    
    gjennomsnitt = sum(rating) / len(rating)
    return round(gjennomsnitt, 1)

eksempel_vare = {
    "navn": "Eksempel vare",
    "rating": [5, 2, 7, 1, 6]
}

gjennomsnitt_rangering = calculate_average_ware_rating(eksempel_vare)
if gjennomsnitt_rangering is not None:
    print(f"Gjennomsnitt rangering er: {gjennomsnitt_rangering}")
else:
    print("Denne varen har ikke fått rangering")
    
    
        
    
        
