from art import logo
import random
from replit import clear


def deal_a_card(player, copy_deck):
    card = copy_deck[random.randint(0, 12)]
    player.append(card)
    if sum(player) == 21 and len(player) == 2:
        return 0
    else:
        return player


def main_game():

    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,]
    global player_cards

    global dealer_cards
    player_cards = []
    dealer_cards = []

    player_cards = deal_a_card(player_cards, deck)
    player_cards = deal_a_card(player_cards, deck)
    dealer_cards = deal_a_card(dealer_cards, deck)
    dealer_cards = deal_a_card(dealer_cards, deck)

    def print_score():

        global player_cards

        global dealer_cards
        
      

        print("You Cards are: ")
        if player_cards == 0:
            playercards = random.shuffle([10,11])
            
        print(player_cards, player_score)
        if (dealer_cards):

            if len(dealer_cards) == 2:
                print("Dealer cards are: ")
                print(f"[{dealer_cards[0]}]", dealer_score - dealer_cards[1])
            else:
                print("Dealer cards are: ")
                print(dealer_cards, dealer_score)

        else:

            temp = [11, 10]
            dealer_cards = random.shuffle(temp)
            print(dealer_cards)
            print("Dealer cards are: ")
            print(f"[{dealer_cards[0]}]", dealer_score - dealer_cards[1])
            dealer_cards = 0
    # 1.print logon
   

    # 2.shuffle deck

    # 3. deal cards.

    if dealer_cards != 0:
        dealer_score = sum(dealer_cards)

    else:
        dealer_score = 21

    if player_cards != 0:
        player_score = sum(player_cards)
    else:
        player_score = 21

    print(logo)
    print("Welcome to play Blackjack: ")
    print_score()

    

    draw_a_card = "y"
    while draw_a_card == "y":
        if player_cards == 0:
            print("You have Black Jack")
            player_score = 21

            draw_a_card = "n"
            print("Now dealing for Dealer")

            if dealer_cards == 0:
                print("dealer has blackjack")
                print("Game is Even")
                dealer_score = 21

                new_game = input("Do you want to play another round? y / n: ")
                if new_game == "y":
                    main_game()

            else:
                while dealer_score < 17:
                    dealer_cards = deal_a_card(dealer_cards, deck)
                    dealer_score = sum(dealer_cards)
                    print_score()
                else:
                    dealer_score = sum(dealer_cards)
                    print_score()

                    print(f"Your score is {player_score}.")
                    print(f"Dealer score is {dealer_score}.")
                    if dealer_score > 21:

                        print("Dealer Bust!, You Win")

                    elif player_score > dealer_score:
                        print("you win!")
                    elif player_score < dealer_score:
                        print("Dealer Wins")
                    else:
                        print("Game is even!")

        else:

            draw_a_card = input("Do you want to draw a card? 'y'/'n'?: ")
            if draw_a_card == "y":
                player_cards = deal_a_card(player_cards, deck)
                player_score = sum(player_cards)
                print_score()
                if player_score > 21:
                    print("You are bust and lose this round.")
                    draw_a_card = "n"
                    new_game = input(
                        "Do you want to play another round? y / n: ")
                    if new_game == "y":
                        main_game()
            else:
                print("Now dealing for Dealer")
                if dealer_cards == 0:
                    print("dealer has blackjack")
                    dealer_score = 21

                else:
                    while dealer_score < 17:
                        dealer_cards = deal_a_card(dealer_cards, deck)
                        dealer_score = sum(dealer_cards)
                        print_score()
                    else:
                        dealer_score = sum(dealer_cards)
                        print_score()

                        print(f"Your score is {player_score}.")
                        print(f"Dealer score is {dealer_score}.")
                        if dealer_score > 21:

                            print("Dealer Bust!, You Win")

                        elif player_score > dealer_score:
                            print("you win!")
                        elif player_score < dealer_score:
                            print("Dealer Wins")
                        else:
                            print("Game is even!")

                new_game = input("Do you want to play another round? y / n: ")
                if new_game == "y":
                    main_game()

    if dealer_score > 21:
        print("Dealer Bust!, You Win")
        new_game = input("Do you want to play another round? y / n: ")
        if new_game == "y":
            main_game()


main_game()
