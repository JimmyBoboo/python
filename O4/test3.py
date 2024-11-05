import blackjack_module as bjm

def spill_runde():
    cards = bjm.get_new_shuffled_deck()
    player, dealer = [], []
    
    # Del ut to kort til spiller og dealer
    for _ in range(2):
        player.append(bjm.get_new_card(cards))
        dealer.append(bjm.get_new_card(cards))
    
    # Vis spillerens kort og dealerens synlige kort
    print(f"\nKortene er delt ut. Du har {player[0]} og {player[1]} med en totalverdi på: {bjm.calculate_hand_value(player)}")
    print(f"Dealeren har et synlig kort {dealer[0]}, med verdi: {bjm.get_card_value(dealer[0])}")
    
    # Sjekk for blackjack
    if bjm.calculate_hand_value(player) == 21:
        print("Gratulerer, du har blackjack! Du vinner!")
        return
    elif bjm.calculate_hand_value(dealer) == 21:
        print("Dealeren har blackjack! Du taper.")
        return
    
    # Spillerens valg: hit eller stand
    while True:
        print("\nØnsker du å trekke eller stå? \n1 - Trekke \n2 - Stå")
        choice = input("> ")
        
        if choice == "1":  # Spiller trekker et kort
            new_card = bjm.get_new_card(cards)
            player.append(new_card)
            player_value = bjm.calculate_hand_value(player)
            
            print(f"Du trakk {new_card}. Din totale verdi er nå: {player_value}")
            
            if player_value == 21:
                print("Gratulerer, du har blackjack! Du vinner!")
                return
            elif player_value > 21:
                print("Du har busta! Du taper.")
                return
            
        elif choice == "2":  # Spiller står, dealer sin tur
            print("Du står. Dealeren trekker nå kort.")
            while bjm.calculate_hand_value(dealer) < 17:
                dealer_card = bjm.get_new_card(cards)
                dealer.append(dealer_card)
                print(f"Dealeren trekker {dealer_card}. Dealeren har nå: {bjm.calculate_hand_value(dealer)}")
            
            dealer_value = bjm.calculate_hand_value(dealer)
            player_value = bjm.calculate_hand_value(player)
            
            # Sjekk vinn- og tapsbetingelser
            if dealer_value > 21:
                print("Dealeren busta! Du vinner!")
            elif dealer_value > player_value:
                print(f"Dealeren har {dealer_value}. Du taper!")
            elif dealer_value < player_value:
                print(f"Du har {player_value} mot dealerens {dealer_value}. Du vinner!")
            else:
                print(f"Både du og dealeren har {player_value}. Det er uavgjort!")
            return
        else:
            print("Ugyldig valg, prøv igjen.")
    
# Hovedløkken for spillet
while True:
    spill_runde()
    play_again = input("Vil du spille igjen? (ja/nei) > ").lower()
    if play_again != "ja":
        print("Takk for at du spilte!")
        break
