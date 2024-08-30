side1 = float(input("skriv inn lengden på første siden: "))
side2 = float (input("skriv inn lengden på andre siden "))
side3 = float (input("skriv inn lengden på den tredje siden"))

#trekanten er like sidet
if side1 == side2 and side2 == side3:
    print ("trekanten er likesidet")

elif side1 == side2 or side2 == side3 or side1 == side3:
    print ("trekanten er likebeint")

elif side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1 : 
    print ("dette er ikke en gyldig trekant")

else: 
    print ("trekanten er uliksidet")

    





 







