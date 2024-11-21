
def add_number_of_ware_to_shopping_cart(ware_key, ware, shopping_cart, number_of_ware=1):
    antall = ware.get("antall", 0)
    
    if antall <= 0:
        print(f"Denne varen '{ware_key}' er dessverre ikke på lager, og kan ikke legges til i handlekurven")
        return
    
    if number_of_ware > antall:
        print(f"Det er kun {antall} igjen, '{ware_key}' er tilgjengelig på lager. ")
        number_of_ware = antall
    else:
        print(f"Det er {number_of_ware} av varen '{ware_key}' Legges til i handlevognen")
        
    if ware_key in shopping_cart:
        shopping_cart[ware_key] += number_of_ware
    else:
        shopping_cart[ware_key] = number_of_ware
    
    ware["Antall"] -= number_of_ware
    print(f"Lageret for '{ware_key}' er nå oppdatert til {ware['antall']}")
    return
    
    