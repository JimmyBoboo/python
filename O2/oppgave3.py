# Opprett en liste med Tolkien sine bøker.
Tolkien_sine_boker = [
    "The hobbit",
    "Farmer giles of ham",
    "The fellowship of ring",
    "The two Tower",
    " The Return of the king",
    "The adventures of tom bombadil",
    "Tree and leaf",
]

print("første 2 bøkene i listen!")
print(Tolkien_sine_boker[0])
print(Tolkien_sine_boker[1])
print("Siste 2 bøker i listen!")
print(Tolkien_sine_boker[5])
print(Tolkien_sine_boker[6])

Tolkien_sine_boker.append("The Silmarillion")
print(Tolkien_sine_boker)

Tolkien_sine_boker.append("Unfinished Tales")
print(Tolkien_sine_boker)

Tolkien_sine_boker.insert(2, "Lord of the rings:")
Tolkien_sine_boker.insert(4, "Lord of the rings:")
Tolkien_sine_boker.insert(6, "Lord of the rings:")
print(Tolkien_sine_boker)

# Sortert på en alfabetisk rekkefølge.
Tolkien_sine_boker.sort()
print(Tolkien_sine_boker)
