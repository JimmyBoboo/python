
with open ("exceptions/filmappe/filtest.txt", "a") as fil:
    while True:
        brukerinput = input("Skriv inn noe: ")
        
        if brukerinput == "q":
            break
        
        
        
        
        fil.write(brukerinput)

