def rent_car_monthly(bilpris, hvis_ny):
    arlig_pris = 0.4 * bilpris
    manedlig_pris = arlig_pris / 12
    if hvis_ny:
        manedlig_pris += 1000
        return round(manedlig_pris, 2)
    
manedlig_pris = rent_car_monthly(300000, True)
print(f"Månedlig rente pris er {manedlig_pris} kr")
    