from art import logo
import random
from replit import clear
def deal_a_card(player, copy_deck):
    card = copy_deck[random.randint(0,12)]
    player.append(card)
    return player

def print_score():
    clear()

    print(logo)
    print("You Cards are: ")
    print(player_cards, player_score)
    print("Dealer cards are: ")
    print(dealer_cards, dealer_score)


deck = [11, 2, 3, 4, 5, 6, 7 , 8 , 9 , 10 , 10 , 10 , 10,]
#1.print logo
print(logo)
print("Welcome to play Blackjack: ")

#2.shuffle deck


#3. deal cards.


player_cards = []
dealer_cards = []

player_cards = deal_a_card(player_cards, deck)
player_cards = deal_a_card(player_cards, deck)
dealer_cards = deal_a_card(dealer_cards, deck)
dealer_cards = deal_a_card(dealer_cards, deck)
dealer_score = sum(dealer_cards)
player_score = sum(player_cards)


print_score()






draw_a_card = "y"
while draw_a_card == "y":
    draw_a_card = input("Do you want to draw a card? 'y'/'n'?: ")
    if  draw_a_card == "y":
        player_cards = deal_a_card(player_cards, deck)
        player_score = sum(player_cards)
        print_score()
        if player_score > 21:
            print("You are bust and lose this round.")
            draw_a_card = "n"
    else:
       print("No dealing for Dealer")
    

