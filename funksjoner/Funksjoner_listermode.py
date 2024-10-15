import random

brettspill = ['Ubongo', 'Pandemic', 'Ludo', 'Monopol', 'Mysterium']
def velg_tilfeldig_brettspill(spillliste):
    indexnummer = random.randrange(len(spillliste))
    return spillliste.pop(indexnummer)

#valgt_brettspill = velg_tilfeldig_brettspill(brettspill)

print(f"Du valgte {velg_tilfeldig_brettspill(brettspill)}")
print(brettspill)


    