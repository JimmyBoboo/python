def calculte_total(menu, order):
    total_price = 0.0
    
    for item, quantity in order.items():
        if item in menu:
            total_price += menu[item] * quantity
            
    return round(total_price, 2)

menu = {
    "ribbe": 145.90,
    "pinnekjøtt": 155.90,
    "lutefisk": 135.90,
    "nøttefisk": 135.90,
    "reindyrstek": 155.90}

order = {
    "ribbe": 3,
    "pinnekjøtt": 0,
    "reinsdyrstek": 0
}

total = calculte_total(menu, order)
print ("totalpris er:", total)

def display_cost(menu, order):
    total_price = 0.0
    
    for item, quantity in order.items():
        if item in menu:
            total_price += menu[item] * quantity
    
    return round(total_price, 2)

total = calculte_total(menu, order)
print("Ribbe - (3) - ", total)

def confirm_order(order_cost):
    print(f"Total prisen blir {order_cost} kr")

    valg = input("Vil du bekrefte, Yes/No?")
    
    if valg == "Yes":
        print("Rudolf er grønn på nesen")
        
    
    elif valg == "No":
        print("Rudolf er Rød på nesen")

confirm_order(order_cost=437)
    

        

    

    




    