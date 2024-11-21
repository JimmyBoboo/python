def is_number_of_ware_in_stock(ware, number_of_ware):
    stock = ware.get("antall", 0)
    return stock >= number_of_ware

eksempel_bruk = {
                'name': 'Example ware',
                'price': 3999,
                'antall': 30,
                'beskrivelse': 'A non existent ware used only for this example'}

print(is_number_of_ware_in_stock(eksempel_bruk, 5))
print(is_number_of_ware_in_stock(eksempel_bruk, 40))