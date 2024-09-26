import random

# Her er kode som gjør at hvert kast skal være mellom 0-21 poeng.
lovlige_poeng = [random.randrange(0, 50) for i in range(0, 50)]


# Her har jeg definert funksjonen, har brukt personer, piler og runder som verdier.
def spill_dart(personer, piler, runder):
    for spiller in range(personer):
        print(f"\nSpiller {spiller + 1 } sin tur:")
        totalPoeng = 0

        for runde in range(runder):
            print(f"\nRunde {runde + 1}: ")
            rundePoeng = 0

            for pil in range(piler):
                kast = random.choice(lovlige_poeng)
                print(f"\n Kast {pil + 1}: {kast} poeng")
                rundePoeng += kast

            totalPoeng += rundePoeng
            print(f"Totalt for runde {runde + 1}: {rundePoeng} poeng")

            print(f"\nSpiller {spiller + 1} sin totale poengsum: {totalPoeng} poeng")

            print(f"\n Spillet er over")


# Her har lagd variabler med int og input, slik at spilleren kan taste inn hva dem ønsker.
personer = int(input("Hvor mange spillere skal spille? "))
piler = int(input("Hvor mange piler skal det kastes per runde? "))
runder = int(input("Hvor mange runder skal dere spille? "))

print("\nVelkommen til dartspillet")
spill_dart(personer, piler, runder)
