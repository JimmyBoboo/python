from random import randint

countries = ["Norway", "Sweden", "Denmark", "Finland", "Iceland"]
capitals = ["Oslo", "Stockholm", "Copenhagen", "Helsinki", "Reykjavik"]
meny_liste = ["1, Test kunnskap", "2, Legg til land", "3, Avslutt"]


def pick_random_country_and_capital(countries, capitals):
    import random

    spot = random.randint(0, len(countries) - 1)
    cou = countries[spot]
    cap = capitals[spot]
    return cou, cap


def guess_capital():
    country, capital = pick_random_country_and_capital(countries, capitals)
    sted = input(f"Hva er hovedstaden i {country}:? ").lower()
    if sted.lower() == capital.lower():
        print("Riktig!")
    else:
        print("Feil!")


# Lage en funksjon som gjør tilsier at man ikke kan legge til det samme landet flere ganger.
def add_country():
    country = input("Hvilket land vil du legge til?")
    if country in countries:
        print("Landet er allerede lagt til")
    else:
        capital = input("Hvilken hovedstad har landet?")
        countries.append(country)
        capitals.append(capital)
        print(f"{country} og {capital} er lagt til! ")
        print(countries, capitals)


def meny():

    while True:
        for i in meny_liste:
            print(i)

        valg = int(input("Hva vil du gjøre?"))

        if valg == 1:
            guess_capital()

        elif valg == 2:
            add_country()

        elif valg == 3:
            break
        else:
            print("hade ogsånn")


# guess_capital()

meny()
