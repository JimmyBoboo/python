def confirm_order(order_cost):
    print(f"Total prisen blir {order_cost} kr")

    valg = input("Vil du bekrefte, Yes/No?")
    
    if valg == "yes":
        print("Rudolf er grønn på nesen")
        return True
        
    
    elif valg == "no":
        print("Rudolf er Rød på nesen")
        return False

confirm_order(order_cost=437)
    