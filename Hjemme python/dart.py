import random

# Definere de lovlige poengene i dart
lovlige_poeng = (
    [0]
    + [i for i in range(1, 21)]
    + [2 * i for i in range(1, 21)]
    + [3 * i for i in range(1, 21)]
    + [25, 50]
)


def spill_dart(spillere, piler_per_runde, runder):
    for spiller in range(spillere):
        print(f"\nSpiller {spiller + 1} sin tur:")
        total_poeng = 0

        for runde in range(runder):
            print(f"\nRunde {runde + 1}:")
            runde_poeng = 0

            for pil in range(piler_per_runde):
                kast = random.choice(lovlige_poeng)
                print(f"Kast {pil + 1}: {kast} poeng")
                runde_poeng += kast

            total_poeng += runde_poeng
            print(f"Totalt for runde {runde + 1}: {runde_poeng} poeng")

        print(f"\nSpiller {spiller + 1} sin totale poengsum: {total_poeng} poeng\n")
    print("Spillet er over!")


# Hente inn antall spillere, piler per runde og antall runder fra brukeren
spillere = int(input("Hvor mange spillere skal spille? "))
piler_per_runde = int(input("Hvor mange piler skal hver spiller kaste per runde? "))
runder = int(input("Hvor mange runder skal spilles? "))

print("\nVelkommen til dartspillet!")
spill_dart(spillere, piler_per_runde, runder)
