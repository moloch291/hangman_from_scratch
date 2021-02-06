import main
import life_status
import os
import time
import string


def loose_message(word):
    os.system('clear')
    print(life_status.get_loose_ascii())
    print("The puzzle was " + word + "...\n")
    life_status.dead_status()
    time.sleep(4.3)
    main.menu()


def win_message():
    os.system('clear')
    print(life_status.get_win_ascii())
    time.sleep(3)
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


def take_a_guess(word):
    guess = " "
    while guess not in string.ascii_letters:
        guess = input("Take a guess and type a letter! ")
        if guess == "quit" or guess == "exit":
            main.menu()
    return guess


def print_mistakes(mistakes):
    print("\nMistakes you already made:")
    if mistakes:
        for mistake in mistakes:
            print(mistake)


def print_board(word, correct_guesses):
    for w in range(0, len(word[0:])):
        if word[w] in correct_guesses:
            print(word[w], end="")
        elif word[w] == " ":
            print(" ", end="")
        else:
            print("_", end="")


def print_gallows_state(ls_indicators, lives):
    if lives == 1:
        print(ls_indicators[5])
    elif lives == 2:
        print(ls_indicators[4])
    elif lives == 3:
        print(ls_indicators[3])
    elif lives == 4:
        print(ls_indicators[2])
    elif lives == 5:
        print(ls_indicators[1])
    elif lives > 5:
        print(ls_indicators[0])


def prepare_round(word, correct_guesses, mistakes, lives, ls_indicators):
    print_gallows_state(ls_indicators, lives)
    print_board(word, correct_guesses)
    print("\n\nYou can make " + str(lives) + " more mistakes before hangtime!")
    print_mistakes(mistakes)


def add_spaces(word):
    correct_guesses = []
    for character in word:
        if character == " ":
            correct_guesses.append(character)
    return correct_guesses


def get_win_conditions(word):
    win_conditions = []
    for character in word:
        win_conditions.append(character)
    win_conditions = sorted(set(win_conditions))
    return win_conditions
