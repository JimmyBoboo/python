brettspill = ["ubongo", "Pandemic", "Ludo", "Monopol", "Mysterium"]

for spill in brettspill:
    print(f"{spill} er et bra spill")

csgo = "Counter strike: Global Offensive"

if csgo not in brettspill:
    brettspill.append(csgo)
    print(f"Legger til {csgo} i brettspillet")
