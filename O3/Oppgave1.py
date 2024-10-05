student = { 
    "fornavn" : "Ola", 
    "etternavn" : "Nordmann",
    "favorittfag" : "Programmering 1" 
} 

x = student ["fornavn"]
y = student ["etternavn"]
print(x, y)

student["favorittfag"] = "ITF10219 Programmering 1"
z = student["favorittfag"]
print (z)

student["alder"] = 21
print(student)
