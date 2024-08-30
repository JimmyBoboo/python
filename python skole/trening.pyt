tall1 = input("Skriv inn et tall: ")
tall2 = input("Skriv inn et tall til: ")
tall3 = input("Skriv inn et tall til: ")

if tall1 == tall2 and tall2 == tall3:
    print('Tallene er like')

elif tall1 != tall2 and tall2 != tall3 and tall1 != tall3:
    print('Tallene er ulike')

elif tall1 == tall2 and tall2 != tall3 or tall1 == tall3 and tall3 != tall2 or tall2 == tall3 and tall3 != tall1:
    print('To av tallene er like')

sum = int(tall1) + int(tall2) + int(tall3)

if sum > 100:
    print('Summen av tallene er over 100')
    
