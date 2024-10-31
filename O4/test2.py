import blackjack_module as bjm
while True:
    cards = bjm.get_new_shuffled_deck()

    player = []
    dealer = []

    for i in range(2):
        playercard = bjm.get_new_card(cards)
        dealercard = bjm.get_new_card(cards)
        player.append(playercard)
        dealer.append(dealercard)
        

    # Kort utdeling av spiller og dealer.    
    print(f"\n The cards have been dealt. You have a {player[0]} and a {player[1]}, \n with a total value of: {bjm.calculate_hand_value(player)}")
    print(f"\n The dealers visible card is a {dealer[0]}, \n with a value of: {bjm.get_card_value(dealer[0])}")

    if bjm.calculate_hand_value(player) == 21:
        print("Congratulations, you have blackjack!")
        
    else:
        while True:
            print("1. Hit")
            print("2. Stand")
            choice = input("> ")
            
            
            if choice == "1":
                playercard = bjm.get_new_card(cards)
                player.append(playercard)
                print(f"You have drawn a {playercard}, You have a total value of: {bjm.calculate_hand_value(player)}")
                bjm.print_result(bjm.calculate_hand_value(player), bjm.calculate_hand_value(dealer))
                break
                
            elif choice == "2":
                print(f"You have a {player[0]} and a {player[1]}  with a total value of {bjm.calculate_hand_value(player)}")
                print(f"The dealers has the cards {dealer[0]} and {dealer[1]} with a value of {bjm.calculate_hand_value(dealer)}")
                bjm.print_result(bjm.calculate_hand_value(player), bjm.calculate_hand_value(dealer))
                break
            
            else:
                print("Invalid choice")
                
            
            
            
                
        play_again = input("Do you want to play again? (yes/no) > ").lower()
        if play_again == "yes":
            continue        
        else:
            print("Invalid choice")
            break

            

