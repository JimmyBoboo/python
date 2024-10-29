import random

def skriver_header():
    print("\n =============================================")
    print("== Hva er din vekt på en annen planet")
    print("================================================")

# Funksjon for å skrive ut planeter.
def skriv_ut_planetliste(planeter_som_skal_skrives_ut):
    for index, planet in enumerate(planeter_som_skal_skrives_ut):
        print(f"{index} - {planet['navn']}")

# Funksjon for tilfeldig planet
def velg_tilfeldig(valgt_samling):
    random_index = random.randrange(1, len(valgt_samling))
    valgt_element = valgt_samling[random_index]
    return valgt_element

def beregn_vekt(din_vekt, planettyngdekraft, jordtyngdekraft=9.807):
    beregnet_vekt = (din_vekt / jordtyngdekraft) * planettyngdekraft
    return round(beregnet_vekt, 2)
    
    
    
def en_gang_til():
    svar = input("Vil du prøve en gang til? (Y/N)")
    return svar.upper() == 'Y'



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

