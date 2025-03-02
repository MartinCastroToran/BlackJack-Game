
import random
import art
import os
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
you_win = False
you_lose = False
restart = "Y"
def start_game():
    print(art.logo)
    user_hand = []
    dealer_hand = []
    total_dealer = 0
    total_user = 0
    for card in range(2):
        random_card_user = cards[random.randint(0,12)]
        user_hand.append(random_card_user)
        total_user += random_card_user
        random_card_dealer = cards[random.randint(0,12)]
        total_dealer += random_card_dealer
        dealer_hand.append(random_card_dealer)
    print(f"\n\nYour cards: {user_hand}, current score: {total_user} \n\n")
    print(f"Computer first card: {dealer_hand[0]} \n\n")
    return [[total_user, total_dealer], user_hand, dealer_hand]
def another_card(hand):
    extra_card = cards[random.randint(0,12)]
    hand.append(extra_card)
    total = sum(hand)
    return total
def ace_change_value(hand):
    hand[hand.index(11)] = 1
    total= sum(hand)
    return total
while restart == "Y":
    totals = start_game()
    user_hand = totals[1]
    dealer_hand = totals[2]
    total_user = totals[0][0]
    total_dealer = totals[0][1]
    if total_user == total_dealer and total_user == 21:
        print("Draw")
    elif total_user == 21:
        print("Win with a Blackjack!")
        print(f"Computer cards: {dealer_hand}, current score: {total_dealer}")
    elif total_dealer == 21:
        print("You lose by a Blackjack")
        print(f"Computer cards: {dealer_hand}, current score: {total_dealer}")
    else:
        flag = False
        while total_user < 21 and flag == False :
            get_another_card = input("Type 'y' to get another card, type 'n' to pass: ").upper()
            if get_another_card == "Y":
                total_user = another_card(user_hand)
                if total_user > 21:
                    if 11 in user_hand:
                        total_user = ace_change_value(user_hand)
                        print(f"Your cards: {user_hand}, current score: {total_user}")
                        print(f"Computer first card: {dealer_hand[0]}")
                    else:
                        you_lose = True
                        flag = True
                else:
                    print(f"Your cards: {user_hand}, current score: {total_user} ")
                    print(f"Computer first card: {dealer_hand[0]}")
            else:
                flag = True
        while total_user > total_dealer and total_dealer <= 21 and you_lose == False:
            total_dealer = another_card(dealer_hand)
            if total_dealer > 21:
                if 11 in dealer_hand:
                    total_dealer = ace_change_value(dealer_hand)
                else:
                    print(f"Your cards: {user_hand}, score: {total_user}")
                    print(f"Computer cards: {dealer_hand}, Computer's score: {total_dealer}")
                    print("\n\nYou win, congratulation!\n\n")
                    you_win = True
        if (you_win == False and you_lose == True) or (total_dealer>total_user and total_dealer < 21):
            print(f"Your cards: {user_hand}, current score: {total_user}")
            print(f"Computer cards: {dealer_hand}, current score: {total_dealer}")
            print("\n\nYou lose\n\n")
            you_lose == True
        elif total_user == total_dealer:
            print(f"Your cards: {user_hand}, current score: {total_user}")
            print(f"Computer cards: {dealer_hand}, current score: {total_dealer}")
            print("\n\nDraw!\n\n")
    restart = input("Do you want to play BlackJack again, Y or N?").upper()




