#Simulere et dartspill. Hvert kast gir mellom 0 og 60 poeng.


print("Velkommen til dartspillet!")
print("Du har 3 kast til sammen, hvert kast gir mellom 0 og 60 poeng.")

#Lage en list med 3 elementer. 

import random
kast = [random.randrange(0, 60, 5), random.randrange(0, 60, 12), random.randrange(0, 60, 3)]
print("Du fikk", kast[0], "poeng på første kast.")
print("Du fikk", kast[1], "poeng på andre kast.")
print("Du fikk", kast[2], "poeng på tredje kast.")
print("Totalt fikk du", sum(kast), "poeng.")
print("Bra jobbet, bedre lykke neste gang!")

#utvid oppgaven til å ta input på hvor mange spillere som skal spille.
#Hver spiller får 3 kast.

spiller = int(input("Hvor mange spillere skal spille? "))
for i in range(spiller):
    print("Spiller", i+1)
    kast = [random.randrange(0, 60, 5), random.randrange(0, 60, 12), random.randrange(0, 60, 3)]
    print("Du fikk", kast[0], "poeng på første kast.")
    print("Du fikk", kast[1], "poeng på andre kast.")
    print("Du fikk", kast[2], "poeng på tredje kast.")
    print("Totalt fikk du", sum(kast), "poeng.")
    print("Bra jobbet, bedre lykke neste gang!")

    






