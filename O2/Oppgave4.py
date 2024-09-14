#itrere gjennom en liste og printe ut elementene i listen.
liste = ["The fellowship of the ring", "The two towers", "The return of the king"]
print("Alternativ 1")
for element in liste:
    print(element)

#alternativ 2
print("Alternativ 2")
for i in range(len(liste)):
    print(liste[i])

print("Alternativ 3")
#alternativ 3
for i in range(0, len(liste)):
    print(liste[i])