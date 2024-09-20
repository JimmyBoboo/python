
#Lage en pakkeliste for når man skal ut å reise
#Lage en program for hvilke valg man kan velge.
#lagd en tekstboks, som forteller hva man skal velge mellom.
def pakkeliste():
    pakkeliste = []

print(""" \n
    Velkommen til pakkeliste! Velg en av dem under: \n
      1) 'Legg' - for å legge til noe i pakkelisten \n
      2) 'Slett' - for å Slette noe i pakkelisten \n
      3) 'Skriv ut' - for å Skrive ut pakkelisten \n
      4) 'Avslutt' - for å Avslutte pakkelisten\n
      """)


valg = input("\nSkriv inn hva du ønsker å gjøre: ").strip().lower()


#Valg 2: Legg til et element i listen
if valg == "legg":
    valg = input("Hva vil du legge til i pakkelisten? ").strip().lower()
    pakkeliste.append(valg)
    print(pakkeliste)  

#Valg 3: Fjern et element fra listen
elif valg == "slett":
    valg = input("Hva vil du slette fra pakkelisten? ").strip()
    if valg in pakkeliste:
        pakkeliste.remove(valg)
        print(f"{valg} er fjernet fra pakkelisten.")
        
#Valg 4: Skriv ut listen
elif valg == "Skriv ut":
    pakkeliste =[]
    print(pakkeliste)




