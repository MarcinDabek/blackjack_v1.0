#Blackjack project
import random

#draws cards from dealer
def dealer_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
#choose two cards for player
def player():
    player_cards = []
    for i in range(0,2):
      player_cards.append(dealer_cards())
    return player_cards
#choose two cards for computer
def computer():
    computer_cards = []
    for i in range(0, 2):
        computer_cards.append(dealer_cards())
    return computer_cards
#check stamnets if don't want take another card
def check_card():
    if player_card_sum == computer_card_sum:
        print("Draw")
    elif player_card_sum == 21:
        print('BlackJack! you win')
    elif computer_card_sum == 21:
        print("Opponent has BlackJack! You lose")
    elif player_card_sum > computer_card_sum and player_card_sum < 21:
        print("You win")
    elif computer_card_sum > 21:
        print("Opponent went over. You win")
    elif player_card_sum > 21:
        print("You went over. You lose")
    else:
        print("You lose")
#final sentence
def final():
    print(f"Your final hand: {player_card}, final score: {player_card_sum}")
    print(F"Computer's final hand: {computer_card}, final score: {computer_card_sum}")

#main code
game_flag = True
while game_flag:

    start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': " )

    if start_game == "y":
        player_card = player()
        computer_card = computer()
        flag = True
        while flag:
            player_card_sum = sum(player_card)
            computer_card_sum = sum(computer_card)
            if player_card_sum > 21:
                final()
                print("You went over. You lose")
                break
            elif player_card_sum == 21:
                final()
                print('BlackJack! you win')
                break
            elif computer_card_sum == 21 :
                final()
                print("Opponent has BlackJack! You lose")
                break
            print(f"Your cards: {player_card},curennt score: {player_card_sum}")
            print(f"Computer first card: {computer_card[0]}")
            continue_card = input("Type 'y' to get another card or type 'n' to pass: ")
            if continue_card == 'y':
                if computer_card_sum < 17:
                    computer_card.append(dealer_cards())
                player_card.append(dealer_cards())
            else:
                flag = False
                final()
                check_card()

    else:
        print("Bye")
        game_flag = False


