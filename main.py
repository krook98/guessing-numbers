import random

import art
from art import logo

#Number Guessing Game Objectives:

# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

number_to_guess = random.randint(1, 100)


def game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard'")
    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 5
    else:
        print("Type 'easy' or 'hard'")

    while attempts > 0:
        print(f"You have {attempts}  remaining to guess the number")
        guess_number = int(input("Make a guess"))
        if guess_number == number_to_guess:
            print("You win!")
            attempts = 0
        elif guess_number > number_to_guess:
            print("Too high.")
        else:
            print("Too low")
        attempts -= 1
        print("Guess again")

    if attempts == 0 and guess_number != number_to_guess:
        print("You lost!")

game()