from planet_funksjoner import *

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
    