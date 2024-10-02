
planeter = ["Merkur", "Venus", "Jorden", "Mars", "Jupiter", "Saturn", "Uranus", "Neptun"]
tyngdekraft = [3.7, 8.87, 9.807, 3.711, 24.79, 10.44, 8.69, 11.15]

kjør = True
while kjør:
    print("\n =============================================")
    print("== Hva er din vekt på en annen planet")
    print("================================================")

    for planetnummer in range(len(planeter)):
        print(f"{planetnummer + 1} - {planeter[planetnummer]}")
        
    valgt_planetnummer = input("\n Velg en planen ved å skrive et tall: ")
    valgt_planetnummer = int(valgt_planetnummer) -1
    
    valgt_planet = planeter [valgt_planetnummer]
    print(f"Du har valgt {valgt_planet}.")
    
    din_vekt = float(input("Hva er din vekt på jorden?: "))
    
    # Utregninger
    jordens_tyngdekraft = tyngdekraft [2]
    din_masse = din_vekt / jordens_tyngdekraft
    din_vekt_på_planet = round(din_masse * tyngdekraft [valgt_planetnummer], 2)
    
    print(f"Din vekt på planeten {valgt_planet} er din {din_vekt_på_planet}, kg, som har tygndekraft {tyngdekraft[valgt_planetnummer]}")
    
    en_gang_til = input("Vil du kjøre programmet en gang til? Y/N ")
    
    kjør = en_gang_til.upper() == "Y"
    
print("Takk for at du spilte!")

    
    
    