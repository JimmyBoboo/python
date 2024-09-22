# if og else

# tatt input fra brukeren og konvertert til heltall.
svar = int(
    input(
        "Hva er det ultimatet spørsmålet om livet, universet og alle ting? Hint: Det er et tall."
    )
)

# Hvis man svarer 42, printer den ut "det stemmer, meningen med livet er 42."
if svar == 42:
    print("Det stemmer, meningen med livet er 42!")

# Sjekker om tallet er mellom større enn 30 og mindre enn 50.
elif svar > 30 and svar < 50:
    print("Nærme, men feil!")

# Hvis ingen av betingelse er oppfylt.
else:
    print("Feil svar")
