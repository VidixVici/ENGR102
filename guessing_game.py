# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: ZACHARY HARBERT
# Section: 562
# Assignment: 10.15 LAB: Guessing game
# Date: 31 OCTOBER 2023
#
#
# YOUR CODE HERE
#
import random

def get_secret_number():
    return 27

def get_user_guess():
    try:
        guess = int(input("What is your guess? "))
        return guess
    except ValueError:
        print("Bad input! Try again: ")
        return get_user_guess2()
    
def get_user_guess2():
    try:
        guess = int(input(""))
        return guess
    except ValueError:
        print("Bad input! Try again: ")
        return get_user_guess2()

def play_game():
    secret_number = get_secret_number()
    num_guesses = 0

    print("Guess the secret number! Hint: it's an integer between 1 and 100...")

    while True:
        user_guess = get_user_guess()
        num_guesses += 1

        if user_guess < secret_number:
            print("Too low!")
        elif user_guess > secret_number:
            print("Too high!")
        else:
            print(f"You guessed it! It took you {num_guesses} guesses.")
            break

if __name__ == "__main__":
    play_game()
