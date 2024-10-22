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
    
    #Evt velge tilfeldig og en tilbakmelding.
    if planetnummer == 0:
        valgt_planet = velg_tilfeldig(planeter)
        print(f"Du fikk planeten {valgt_planet['navn']}")
        #Velge et tilfeldig planet for brukeren
    
    else:
        valgt_planet = planeter[planetnummer]
        print(f"Du har valgt planeten {valgt_planet['navn']}")
        
        #Ta input med vekt
    Brukervekt = float(input(f"Hva er din vekt på jorden?: "))


    #Beregninger
    vekt_pa_en_annen_planet = beregn_vekt(Brukervekt, valgt_planet ['tyngdekraft'])
    
    
    #Tilbakemelding
    print(f"Din vekt på planeten {valgt_planet['navn']} med tyngdekraft {valgt_planet['tyngdekraft']} er: {vekt_pa_en_annen_planet} kg. ")
    
    #Ta input om avslutning
    
    run = en_gang_til()
    