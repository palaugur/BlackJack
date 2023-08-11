import random
import os

cards = [
    {
        "Hearts": ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    },
    {
        "Diamonds": ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    },
    {
        "Clubs": ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    },
    {
        "Spades": ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    }
]


# Function to clear the console
def clear_console():
    os.system('cls')


# Function to draw cards from the card list above
def draw_card():
    choice_color = cards[random.randint(0, 3)]
    for key in choice_color:
        card = random.choice(choice_color[key])
        index = choice_color[key].index(card)
        choice_color[key].pop(index)

        # To check during coding
        # print("******************************")
        # print(f"Color = {key}, Card = {card}")
        # print(cards)
        # print("******************************")

        return key, card


#Score calculation function using computer card list or user card list
def calculate_score(card_list):
    result = 0
    ace_counter = 0
    for i in range(0, len(card_list)):
        if card_list[i][1] == "Jack" or card_list[i][1] == "Queen" or card_list[i][1] == "King":
            result += 10
        elif card_list[i][1] == "Ace":
            ace_counter += 1
        else:
            result += int(card_list[i][1])

    for i in range(ace_counter):
        if result + 10 > 21:
            result += 1
        else:
            result += 11
    return result


# Function to format the card list view
def format_card_view(card_list, hasHidden):
    text = ""
    for element in card_list:
        if not hasHidden:
            text += f"|{element[0]}-{element[1]}|\t"
        if hasHidden:
            text = f"|{element[0]}-{element[1]}|\t |Hidden|"

    return text


# Function to write user and computer cards to the console
def print_cards(user_list, computer_list, hasHidden):
    user_card_list = format_card_view(user_list, False)

    if hasHidden:
        computer_card_list = format_card_view(computer_list, True)
    else:
        computer_card_list = format_card_view(computer_list, False)

    print(f"Computer Cards: {computer_card_list}")
    print(f"User Cards    : {user_card_list}")
    print(f"User Points   : {calculate_score(user_list)}")
