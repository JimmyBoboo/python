#Mini Kalkulator, operator.

#Lagd funksjoner, slik at programmet vet hvordan den skal regne.
def add(x, y):
    print(x + y)

def subtract(x, y):
    print(x - y)

def multiply(x, y):
    print(x * y)

def divide(x, y):
    print(x / y)

def modulo(x, y):
    print(x % y)

def opphøye(x, y):
    print(x ** y)

def deleRound(x, y):
    print(x // y)

#lagd en tekstboks, som forteller hva man skal velge mellom.
print(""" \n
    Velg en av dem under (1-7): \n
      1) Pluss \n
      2) Minus \n
      3) Gange \n
      4) Dele \n 
      5) Modulo \n
      6) Opphøye \n
      7) Dele med nedrunding \n
      """)

#lagd en variabel med datatypen int. 
velg = int(input("Velg tall mellom 1-7 "))

x = int(input("Første nr: "))
y = int(input("Andre nr: "))

#lagd funksjon slik at hvis man velger et av valgene under, vil den lese funksjonen som er lagd tidligere regne ut riktig måte.
if velg == 1:
    add(x,y)
elif velg == 2:
    subtract(x,y)
elif velg == 3:
    multiply (x,y)
elif velg == 4:
    divide(x,y)
elif velg == 5:
    modulo(x,y)
elif velg == 6:
    opphøye(x,y)
elif velg == 7:
    deleRound(x,y)
else:
    print("Ugyldig")



