#Rock, Paper, Scissors Game

import random
from enum import IntEnum

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

# this will returns the user selected action
def get_user_selection():
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    selection = int(input(f"Enter a choice ({choices_str}): "))
    action = Action(selection)
    return action

def get_computer_selection():
    selection = random.randint(0, len(Action)-1)
    action = Action(selection)
    return action

def determine_winner(user_action, computer_action):
    if user_action == computer_action:
        print(f"Both player slected {user_action.name} It's a tie!")
    elif user_action == Action.Rock:
        if computer_action == Action.Scissors:
            print("Rock smashes scissors! You Lose!")
        else:
            print("Paper cover rock! You win!")
    elif user_action == Action.Paper:
        if computer_action == Action.Rock:
            print("Paper cover rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == Action.Scissors:
        if computer_action == Action.Paper:
            print("Scissors cut paper! You win!")
        else:
            print("Rock Smashes scissors! You lose.")

while True:
    try:
        user_action = get_user_selection()
    except ValueError as e:
        range_str = f"[0, {len(Action) - 1}]"
        print(f"Invalid selection. Enter a value in range {range_str}")
        continue
    
    computer_action = get_computer_selection()
    determine_winner(user_action, computer_action)

#This condtion will determine if the user want to play again
    play_again = input("Play Again? (y/n): ")
    if play_again.lower() == "n":
        print("Thank you for playing!")
        break
    elif play_again.lower() != "y":
        print("Invalid option, ending game")
        break