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
        