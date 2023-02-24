import random
from os import system
from art import *
#system('cls')



print("Welcome to black jack game 😍")

def deal_card():
    """return random card"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)


def calculate_sum(cards):
    """calculate the sum of cards"""
    #black jack condition
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    #check if ace present
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        return sum(cards)

    return sum(cards)
    

def compare(user_score,dealer_score):
        if dealer_score == 0:
            return "lose opponent has a black jack"
        elif user_score == 0:
            return "win with a black jack "
        elif dealer_score > 21 and user_score > 21:
            return "you went over"
        elif user_score > 21:
            return "you went over you lose"
        elif dealer_score > 21:
            return "dealer win opponent went over"
        elif user_score > dealer_score:
            return "you win"
        else:
            return "you lose"
            


def play_game():
    print(logo1)
    user_card = []
    dealer_card = []

    ##initially choose two card for both user and dealer
    for _ in range(2):
        user_card.append(deal_card())
        dealer_card.append(deal_card())


    game_over = False

    while not game_over:
        user_sum = calculate_sum(user_card)
        dealer_sum = calculate_sum(dealer_card)

        if user_sum == 0 or dealer_sum == 0:
            game_over = True
        else:
            print(f"your card {user_card} and current score : {user_sum}")
            print(f"dealer card {dealer_card[0]}")


            if input("do you want to add more cards 'y' or 'n' : ").lower() == "y":
                user_card.append(deal_card())
            else:
                game_over = True


    ### add dealer card now till sum < 17

    while dealer_sum != 0 and dealer_sum < 17:
        dealer_card.append(deal_card())
        dealer_sum = calculate_sum(dealer_card)


    print(f"your card {user_card} and current score : {user_sum}")
    print(f"dealer card {dealer_card} and dealer score : {dealer_sum}")

    print(compare(user_sum,dealer_sum))

while input("do you want to play again 'y' or 'n': ") == "y":
    system('cls')
    play_game()
