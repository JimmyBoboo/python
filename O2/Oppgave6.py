
#Lage en pakkeliste for når man skal ut å reise

#Lager en funksjon som heter pakkeliste

pakkeliste = []
#lagd en tekstboks, som forteller hva man skal velge mellom.
print(""" \n
Velkommen til pakkeliste! Velg en av dem under: \n
    1) 'Legg' - for å legge til noe i pakkelisten \n
    2) 'Slett' - for å Slette noe i pakkelisten \n
    3) 'Skriv ut' - for å Skrive ut pakkelisten \n
    4) 'Avslutt' - for å Avslutte pakkelisten\n
    """)

#Lager en while-løkke som kjører så lenge brukeren ikke har valgt å avslutte programmet.
while True:

    valg = input("Hva vil du gjøre? ")


#Valg 2: Legg til et element i listen
    if valg == "1":
        element = input("Hva vil du legge til i pakkelisten? ")
        pakkeliste.append(element)
        print(f"{element} er lagt til i pakkelisten.")  
#valg 3: Slett et element i listen
    elif valg == "2":
        element = input("Hva vil du slette fra pakkelisten? ")
        if element in pakkeliste:
            pakkeliste.remove(element)
            print(f"{element} er fjernet fra pakkelisten.")
        else:
            print(f"{element} er ikke i pakkelisten.")
    
    elif valg == "3":
        print("Pakkelisten din:")
        for element in pakkeliste:
            print(f"- {element}")

#Valg 4: Avslutt programmet
    elif valg == "4":
        print("Ha en fin reise!")
        break

    else:
        print("Ugyldig valg. Prøv igjen.")
        






