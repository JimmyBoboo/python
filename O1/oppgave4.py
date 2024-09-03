#Variabler
a = 6
b = 3
c = 2

#Regnestykket
result_a = a + b * c        #a + b * c 
result_b = (a + b) * c      #(a + b) * c
result_c = a / b / c        #a / b / c
result_d = a / (b / c)      #a / (b / c)

#Her legger printer vi ut regnestykket ved bruk av variablene og funksjonen som er satt opp.
#Her har jeg også lagt inn en string.
print(f"{a} + {b} * {c} = " + str(result_a))
print(f"({a} + {b}) * {c} =", result_b)
print(f"{a} / {b} / {c} =", result_c)
print(f"{a} / ({b} / {c}) =", result_d)




