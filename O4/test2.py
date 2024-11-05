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

    # Muligheter for hva som skjer
    if bjm.calculate_hand_value(player) == 21:
        print("Congratulations, you have blackjack!")
        
    elif bjm.calculate_hand_value(dealer) == 21:
        print("Dealeren fikk blackjack, du har tapt!")
    
    elif bjm.calculate_hand_value(dealer) > bjm.calculate_hand_value(player):
        print(f"Dealeren fikk {bjm.calculate_hand_value(dealer)}, du taper!")
        
        
    else:
        while True:
            print("\n Do you wish to hit or stand? \n 1 - Hit \n 2 - Stand")
            choice = input("> ")
            
            
            if choice == "1":
                playercard = bjm.get_new_card(cards)
                player.append(playercard)
                # # print(f"You have drawn a {playercard}, You have a total value of: {bjm.calculate_hand_value(player)}")
                #Hvis spilleren har under 21, vil den fortsette å spørre om å trekke eller stå. 
                if bjm.calculate_hand_value(player) < 21:
                    print (f"Du fikk {playercard}, og har tilsammen: {bjm.calculate_hand_value(player)}, vil stå eller trekke?")
                #Hvis spilleren får 21, vinner den!
                elif bjm.calculate_hand_value(player) == 21:
                    print(f"Du fikk blackjack. Du Vinner!!")
                elif bjm.calculate_hand_value(player) > 21:
                    print(f"Du har Busta! Du fikk {bjm.calculate_hand_value(player)}")
                    break
                # bjm.print_result(bjm.calculate_hand_value(player), bjm.calculate_hand_value(dealer))
                
                    
                    
                
            elif choice == "2":
                # print(f"You have a {player[0]} and a {player[1]}  with a total value of {bjm.calculate_hand_value(player)}")
                # print(f"The dealers has the cards {dealer[0]} and {dealer[1]} with a value of {bjm.calculate_hand_value(dealer)}")
                
                while bjm.calculate_hand_value(dealer) < 17:
                    nytt_kort_Dealer = bjm.get_new_card(cards)
                    dealer.append(nytt_kort_Dealer)
                    print(f"Dealeren fikk {nytt_kort_Dealer}, Dealeren har totalt: {bjm.calculate_hand_value(dealer)}")
                # bjm.print_result(bjm.calculate_hand_value(player), bjm.calculate_hand_value(dealer))
                break
            
           
            else:
                print("Invalid choice")
                
                
        play_again = input("Do you want to play again? (yes/no) > ").lower()
        if play_again == "yes":
            continue        
        else:
            print("Invalid choice")
            break

            

