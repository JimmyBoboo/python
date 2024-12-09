
def gange (x, y):
    print (x * y)
    
def dele (x, y):
    print (x / y)
    
def pluss (x, y):
    print (x + y)
    
def minus (x, y):
    print (x - y)

def modulo (x, y):
    print (x % y)
    
def opphøye (x, y):
    print (x ** y)

def dele_med_nedrunding (x, y):
    print (x // y)
    
print (""" velkommen til kalkulator, hva ønsker du å gjøre? \n
       1. gange \n
       2. dele \n
       3. plusse \n
       4. minus \n
       5. modulo \n
       6. opphøye \n
       7. dele med nedrunding \n
       """)

valg = int(input("Velg mellom 1-7"))

x = int(input("Første nr: "))
y = int(input("Andre nr: "))

if valg == 1:
    gange (x,y)

elif valg == 2:
    dele (x, y)

elif valg == 3:
    pluss(x, y)
    
elif valg == 4:
    minus (x, y)

elif valg == 5:
    modulo (x, y)

elif valg == 6:
    opphøye(x, y)
    
elif valg == 7:
    dele_med_nedrunding (x, y)

else:
    print("Ugyldig valg")