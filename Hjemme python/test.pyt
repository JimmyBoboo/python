def pakkeliste_program():
    pakkeliste = []  # Tom pakkeliste

    print("Velkommen til pakkeliste-programmet!")
    print("Kommandoer:")
    print("'legg' - Legg til noe i pakkelisten")
    print("'slett' - Slett noe fra pakkelisten")
    print("'vis' - Vis hele pakkelisten")
    print("'avslutt' - Avslutt programmet")
    
    while True:
        kommando = input("\nSkriv inn en kommando: ").strip().lower()

        if kommando == "legg":
            item = input("Hva vil du legge til? ").strip()
            pakkeliste.append(item)
            print(f"'{item}' er lagt til i pakkelisten.")

        elif kommando == "slett":
            item = input("Hva vil du slette? ").strip()
            if item in pakkeliste:
                pakkeliste.remove(item)
                print(f"'{item}' er slettet fra pakkelisten.")
            else:
                print(f"'{item}' finnes ikke i pakkelisten.")

        elif kommando == "vis":
            if pakkeliste:
                print("Pakkelisten din:")
                for i, item in enumerate(pakkeliste, start=1):
                    print(f"{i}. {item}")
            else:
                print("Pakkelisten er tom.")

        elif kommando == "avslutt":
            print("Avslutter programmet.")
            break

        else:
            print("Ugyldig kommando. Prøv igjen.")

# Kjør programmet
pakkeliste_program()




