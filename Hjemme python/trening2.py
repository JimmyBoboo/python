kjør = True
while kjør:
    print("test")
    for nummer in range(2):
        print(nummer)
    en_gang_til = input("Skrive ut en gang til? Y/N")
    kjør = en_gang_til.upper() == "Y"
