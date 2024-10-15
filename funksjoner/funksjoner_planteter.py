


def skriver_header():
    print("\n =============================================")
    print("== Hva er din vekt på en annen planet")
    print("================================================")


def skriv_ut_planetliste(planeter_som_skal_skrives_ut):
    for index, planet in enumerate(planeter_som_skal_skrives_ut):
        print(f"{index} - {planet['navn']}")


planeter = [
    {'navn': 'Tilfeldig planet'},
    {'navn': 'Merkur', 'tyngdekraft': 3.7},
    {'navn': 'Venus', 'tyngdekraft': 8.87},
    {'navn': 'Jorden', 'tyngdekraft': 9.807},
    {'navn': 'Mars', 'tyngdekraft': 3.711},
    {'navn': 'Jupiter', 'tyngdekraft': 24.79},
    {'navn': 'Saturn', 'tyngdekraft': 10.44},
    {'navn': 'Uranus', 'tyngdekraft': 8.69},
    {'navn': 'Neptun', 'tyngdekraft': 11.15}
]



#-----------------------------
run = True
while run == True:

# "PSEUKODE"
    
    #Skrive ut overskrift
    skriver_header()
    
    #Skrive ut liste over planetene
    skriv_ut_planetliste(planeter)
    
    #Ta input som valg, og en tilbakemelding
    planetnummer = int(input("\n Velg en mellom planet ved å skrive inn et tall: "))
    
    #Ta input med vekt
    #Beregninger
    #Tilbakemelding
    
    #Ta input om avslutning
    
    run = False
    