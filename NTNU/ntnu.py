# Lag en funksjonen guess_capital
from random import randint

countries = ["Norway", "Sweden", "Denmark", "Finland", "Iceland"]
capitals = ["Oslo", "Stockholm", "Copenhagen", "Helsinki", "Reykjavik"]


def guess_capital():
    import random

    a = random.randint(0, len(countries) - 1)
    sted = input(f"Hva er hovedstaden i {countries[a]}:? ").lower()
    if sted == capitals[a].lower():
        print("Riktig!")
    else:
        print("Feil!")


guess_capital()
