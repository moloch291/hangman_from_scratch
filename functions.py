import main
import os
import time


def loose_message():
    os.system('clear')
    print("You lost!")
    time.sleep(2)
    main.menu()


def win_message():
    os.system('clear')
    print("You won!")
    time.sleep(2)
    main.menu()


def win_check(win_conditions, correct_guesses):
    if correct_guesses:
        if set(win_conditions) == set(correct_guesses):
            return True
        else:
            return False


def win_check_system(win_conditions, correct_guesses):
    if win_check(win_conditions, correct_guesses):
        win_message()


def check_guess(guess, win_conditions):
    if guess in win_conditions:
        return True
    else:
        return False


def take_a_guess():
    guess = input("Take a guess!\n")
    if guess == "quit" or guess == "exit":
        main.menu()
    return guess


def print_mistakes(mistakes):
    print("Mistakes:")
    if mistakes:
        for mistake in mistakes:
            print(mistake)


def print_correct_guesses(correct_guesses):
    print("\nCorrect guesses so far:")
    if correct_guesses:
        for guess in correct_guesses:
            print(guess)


def print_board(word, correct_guesses):
    for w in range(0, len(word[0:])):
        if word[w] in correct_guesses:
            print(word[w], end="")
        elif word[w] == " ":
            print(" ", end="")
        else:
            print("_", end="")


def get_win_conditions(word):
    win_conditions = []
    for character in word:
        win_conditions.append(character)
    win_conditions = sorted(set(win_conditions))
    return win_conditions
