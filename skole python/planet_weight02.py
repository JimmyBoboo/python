
planter = ["Merkur", "Venus", "Jorden", "Mars", "Jupiter", "Saturn", "Uranus", "Neptun"]
tyngdekraft = [3.7, 8.87, 9.807, 3.711, 24.79, 10.44, 8.69, 11.15]

print("----Planeter-----")
print("1 - Merkur")
print("2 - Venus")
print("3 - Jorden")
print("4 - Mars")
print("5 - Jupiter")
print("6 - Saturn")
print("7 - Uranus")
print("8 - Neptun")

planetnummer = int(input("Velg en planet nummer fra 1-8: "))

if (planetnummer <= 0 or planetnummer > len(planter)):
    print("Ugyldig valg")
    exit()

planetnummer = planetnummer - 1
print(f"Du valgte planeten {planter[planetnummer]}")

din_Vekt =(input("Hva er din vekt på jorden (i hele kg)? "))
din_Vekt = int(din_Vekt)

din_masse = din_Vekt / tyngdekraft[2]
vekt_paa_planet = din_masse * tyngdekraft[planetnummer]

print(f"Din vekt på {planter[planetnummer]} er {round(vekt_paa_planet, 2)} kg")
