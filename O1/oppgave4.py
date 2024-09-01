#Lag tre variabler: a=6, b=3, c=2

#Definer variablene
a = 6
b = 3
c = 2

#Regnestykket
result_a = a + b * c        #a + b * c 
result_b = (a + b) * c      #(a + b) * c
result_c = a / b / c        #a / b / c
result_d = a / (b / c)      #a / (b / c)

#Her 
print(f"{a} + {b} * {c} = " + str(result_a))
print(f"({a} + {b}) * {c} =", result_b)
print(f"{a} / {b} / {c} =", result_c)
print(f"{a} / ({b} / {c}) =", result_d)




