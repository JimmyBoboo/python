
def print_ware_information(ware):
    print(f"Name: {ware['name']}")
    print(f"Price: {ware['price']},-")
    print(f"Number in Stock: {ware['antall']}")
    print(f"Description: {ware['beskrivelse']}")
    


eksempel_bruk = {
                'name': 'Example ware',
                'price': 3999,
                'antall': 30,
                'beskrivelse': 'A non existent ware used only for this example'}


print_ware_information(eksempel_bruk)

