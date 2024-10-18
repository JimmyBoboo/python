
try: 
    tall1 = int(input("Skriv inn et tall: "))
    tall2 = int(input("Skriv inn et tall til: "))
    svar = tall1 / tall2

    
except ValueError: 
    print(f"Du skrev inn en ugyldg verdi. ")


except NameError:
    print("Kunne ikke regne ut svar")
    
except ZeroDivisionError:
    print("0 kan ikke deles på")
    
else: 
    print(svar)