import json


def save_order_to_file(file_name, order):
     with open(file_name, "w") as f:
         for x in order:
             liste = (f"\n {x} - kr")
             f.write(liste)
             print(f"Ordrene er skreve til {file_name}")
        
file_name = "ordre"

order = {"reinsdyrkjott": 3,
    "lutefisk": 0,
    "ribbe": 0}


# save_order_to_file(file_name, order)

def save_order(file_name, order):
    with open (file_name, "w") as f:
        json.dump(order, f, indent=4)

save_order(file_name, order)

def load_order_from_file(file_name):
    with open (file_name, "r") as f:
        ordre_fra_list = json.load(f)
        print(ordre_fra_list)
        print(type(ordre_fra_list))
    
load_order_from_file(file_name)


        
