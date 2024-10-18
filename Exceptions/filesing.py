
with open("zenpython.txt") as fil:
    innhold = fil.read()
    print(type(innhold))
    
with open("zenpython.txt") as ny_fil:
    linjeliste = ny_fil.readlines()
    print(linjeliste)
    print(type(linjeliste))
    
with open("zenpython.txt") as fil:
    print(f"\n {fil.readline()} - Første linje")
    print(f"\n {fil.readline()} - Andre linje")
    print(f"\n {fil.readline()} - Tredje linje")

filnavn = "Exceptions/filmappe/test.txt"

try:
    with open (filnavn) as fil:
        print(f"{fil.readline()} - Første linje")
except FileNotFoundError:
    print("Denne filen finnes ikke")