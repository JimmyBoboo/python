import json

planeter = [
    {'navn': 'Tilfeldig planet'},
    {'navn': 'Merkur', 'tyngdekraft': 3.7},
    {'navn': 'Venus', 'tyngdekraft': 8.87},
    {'navn': 'Jorden', 'tyngdekraft': 9.807}
]


filnavn = "planeter.json"
with open (filnavn, "w") as utfil:
    json.dump(planeter, utfil, indent=4)

with open (filnavn, "r") as fil:
    planeter_fra_fil = json.load(fil)
    print(planeter_fra_fil)
    print(type(planeter_fra_fil))
    
json_string = '{"dyr": "Hund", "navn": "Fido", "alder": "10"}'
print(json_string)
print(type(json_string))

hund = json.loads(json_string)
print(hund)
print(type(hund))
print(f"Hunden {hund['navn']} er {hund['alder']} år gammel. ")