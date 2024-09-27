student = { 
    "fornavn" : "Ola", 
    "etternavn" : "Nordmann",
    "favorittfag" : "Programmering 1" 
} 

x = student ["fornavn"]
y = student ["etternavn"]
print(x, y)

z = student["favorittfag"] = "ITF10219 Programmering 1"
print (z)

student["alder"] = 21
print(student)
