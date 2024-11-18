# -------------------Oppgave 1------------------------------------------
def print_ware_information(ware):
    print(f"Name: {ware['name']}")
    print(f"Price: {ware['price']},-")
    print(f"Number in Stock: {ware['antall']}")
    print(f"Description: {ware['beskrivelse']}")
    
# -------------------Oppgave 2------------------------------------------
def calculate_average_ware_rating(ware):                        
    rating = ware.get("rating", [])
    
    if not rating: #Dette er for å se om listen er tom.
        return None
    
    gjennomsnitt = sum(rating) / len(rating)
    return round(gjennomsnitt, 1)                                       

# eksempel_vare = {
#     "navn": "Eksempel vare",
#     "rating": [5, 2, 7, 1, 6]
# }

# gjennomsnitt_rangering = calculate_average_ware_rating(eksempel_vare)
# if gjennomsnitt_rangering is not None:
#     print(f"Gjennomsnitt rangering er: {gjennomsnitt_rangering}")
# else:
#     print("Denne varen har ikke fått rangering")
# -------------------Oppgave 3-----------------------------------------









# -------------------Oppgave 4-----------------------------------------

def is_number_of_ware_in_stock(ware, number_of_ware):
    stock = ware.get("antall", 0)
    return stock >= number_of_ware

# eksempel_bruk = {
#                 'name': 'Example ware',
#                 'price': 3999,
#                 'antall': 30,
#                 'beskrivelse': 'A non existent ware used only for this example'}

# print(is_number_of_ware_in_stock(eksempel_bruk, 5))
# print(is_number_of_ware_in_stock(eksempel_bruk, 40))

# -------------------Oppgave 5-----------------------------------------
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
# -------------------Oppgave 6-----------------------------------------
def calculate_shopping_cart_price(shopping_cart, all_wares, tax=25.0):
    total_price = 0.0
    
    for ware_key, antall in shopping_cart.items():
        if ware_key in all_wares:
            prisPerTing = all_wares[ware_key]("pris")
            total_price += prisPerTing * antall
        else:
            print("Denne varen finnes ikke på lageret vårt.")
            
        total_pris_med_tax = total_price * (tax / 100)
        return round(total_pris_med_tax, 2)
        