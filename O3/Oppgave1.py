student = { 
    "fornavn" : "Ola", 
    "etternavn" : "Nordmann",
    "favorittfag" : "Programmering 1" 
}
#Skriv ut studentes navn og etternavn. 
x = student ["fornavn"]
y = student ["etternavn"]
print("****1.*****")
print(x, y)
#Endre studentes favoritt fag til ITF10219 Programmering 1.
print("*****2.*****")
student["favorittfag"] = "ITF10219 Programmering 1"
z = student["favorittfag"]
print (z)
#Legge til alder.
print("****3.****")
student["alder"] = 21
print(student)


