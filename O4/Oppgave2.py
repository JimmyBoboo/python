import blackjack_module as bjm
def spill_runde(penger):
    cards = bjm.get_new_shuffled_deck()

    player = []
    dealer = []

    for _ in range(2):
        playercard = bjm.get_new_card(cards)
        dealercard = bjm.get_new_card(cards)
        player.append(playercard)
        dealer.append(dealercard)
    
    print("Velkommen til BlackJack!")
    while True:
        try:
            innsats = int(input(f"Du har {penger} kr. \nHvor mye vil du satse? "))
            if innsats > penger or innsats < 0:
                print("Du har ikke nok penger.")
            else:
                break
        except ValueError:
            print("Ugyldig input. Vennligst skriv inn et tall.")
        

    # Kort utdeling av spiller og dealer.    
    print(f"\n Kortene har blitt utdelt og du fikk: {player[0]} og {player[1]}, \n totalen er: {bjm.calculate_hand_value(player)}")
    print(f"\n Dealer sitt kort er: {dealer[0]}, \n totalen er: {bjm.get_card_value(dealer[0])}")

    # Muligheter for hva som skjer
    if bjm.calculate_hand_value(player) == 21:
        print("Gratulerer du fikk blackjack!")
        return penger + innsats
    # elif bjm.calculate_hand_value(dealer) == 21:
    #     print("Dealeren fikk blackjack, du har tapt!")
    #     return penger - innsats

    # Spillerens valg: hit eller stand
    while True:
            print("\n Ønsker du å trekke eller å stå? \n 1 - Trekke \n 2 - Stå")
            choice = input("> ")
            
            # valg 1: Spiller trekker et kort
            if choice == "1":
                playercard = bjm.get_new_card(cards)
                player.append(playercard)
                nytt_kort_player = bjm.calculate_hand_value(player)

                print(f"Du trakk {playercard}. Din totale verdi er nå: {nytt_kort_player}")

                if nytt_kort_player == 21:
                    print("Gratulerer, du har blackjack! Du vinner!")
                    return penger + innsats
                elif nytt_kort_player > 21:
                    print("Du har busta! Du taper.")
                    return penger - innsats

                
            # valg 2: Spiller står, dealer sin tur
            elif choice == "2":
                print("Du står. Dealeren trekker nå kort.")
                
                while bjm.calculate_hand_value(dealer) < 17:
                    nytt_kort_Dealer = bjm.get_new_card(cards)
                    dealer.append(nytt_kort_Dealer)
                    print(f"Dealeren fikk {nytt_kort_Dealer}, Dealeren har totalt: {bjm.calculate_hand_value(dealer)}")

                nytt_kort_Dealer = bjm.calculate_hand_value(dealer)
                nytt_kort_player = bjm.calculate_hand_value(player)

                if nytt_kort_Dealer > 21:
                    print("Dealeren busta! Du vinner!")
                    return penger + innsats
                
                elif bjm.calculate_hand_value(dealer) == 21:
                    print("Dealeren fikk blackjack, du har tapt!")
                    return penger - innsats
                
                elif nytt_kort_Dealer > nytt_kort_player:
                    print(f"Dealeren har {nytt_kort_Dealer}. Du taper!")
                    return penger - innsats
                
                elif nytt_kort_Dealer < nytt_kort_player:
                    print(f"Du har {nytt_kort_player} mot dealerens {nytt_kort_Dealer}. Du vinner!")
                    return penger + innsats
                
                else: 
                    print(f"Du og dealer har {nytt_kort_player}, det er uavgjort!")
                return penger
            else:
                print("Ugyldig valg")
                
penger = 500           
while penger > 0:
    penger = spill_runde(penger)
    print(f"Du har nå {penger} kr.")
    
    if penger <= 0:
        print("Du har gått tom for penger. Spillet er over.")
        break
    
              
    play_again = input("Vil du spille fortsette? (Ja/Nei) > ").lower()
    if play_again != "ja":
        if play_again == "nei":
            print("Takk for at du spilte!")
        break

    