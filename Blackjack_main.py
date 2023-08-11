import time
from Blackjack_functions import *
from Blackjack_art import *

print(welcome_screen)

isFinished = False
computer_cards = []
user_cards = []

# Both of us  draw two card
for i in range(2):
    computer_cards.append(draw_card())
    user_cards.append(draw_card())

# After each card draw, the cards in our hand are printed on the screen.
print_cards(user_list=user_cards, computer_list=computer_cards, hasHidden=True)

# If we reach 21 points with the first two cards Blackjack! The rest of the code doesn't work.
if calculate_score(user_cards) == 21:
    print(blackjack_win)
    isFinished = True

while not isFinished:
    # Each time we are asked to draw a card, after we answer, the console is cleared and a new screen is printed.
    new_card = input("Do you want new card? Type 'yes' or 'no'.:  ")
    clear_console()

    if new_card == "yes":
        user_cards.append(draw_card())
        print("------------------------------------------")
        print(f"Your new card: {user_cards[-1]}")
        time.sleep(1)
        print_cards(user_list=user_cards, computer_list=computer_cards, hasHidden=True)
        time.sleep(1)
        if calculate_score(user_cards) > 21:
            print(lose)
            break
    elif new_card == "no":
        while calculate_score(computer_cards) < 17:
            computer_cards.append(draw_card())
            print("------------------------------------------")
            print(f"Computer new card: {computer_cards[-1]}")
            time.sleep(1)
            print_cards(user_list=user_cards, computer_list=computer_cards, hasHidden=False)
            time.sleep(1)
            clear_console()

        if calculate_score(computer_cards) == calculate_score(user_cards):
            print(f"Computer Points: {calculate_score(computer_cards)}\nUser Points    : {calculate_score(user_cards)}")
            print("*** Draw! ***")
            isFinished = True
        elif calculate_score(computer_cards) == 21 or calculate_score(user_cards) < calculate_score(computer_cards) <= 21:
            print_cards(user_list=user_cards, computer_list=computer_cards, hasHidden=False)
            print(f"Computer Points: {calculate_score(computer_cards)}")
            print(computer_wins)
            isFinished = True
        else:
            print(f"Computer Points: {calculate_score(computer_cards)}\nUser Points    : {calculate_score(user_cards)}")
            print(win)
            isFinished = True

    else:
        print("Invalid Value!")
