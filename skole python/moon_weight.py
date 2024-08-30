#input bli tolket som en String, float gjør slik at det kan bli konvertert til desimaltall.
my_earth_weight = input ("Hva er din vekt på jorden?")

my_earth_weight = float (my_earth_weight)

earth_Gravity = 9.807
moon_gravity = 1.622

moon_weight = my_earth_weight / earth_Gravity * moon_gravity

print (f"Din vekt på månen er: {moon_weight} kg" )

