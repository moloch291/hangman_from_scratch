import functions
import life_status
import random
import os
import time


def play(word, lives, ls_indicators):
    win_conditions = functions.get_win_conditions(word)
    correct_guesses = functions.add_spaces(word)
    mistakes = []
    while lives > 0:
        os.system('clear')
        functions.prepare_round(
            word, correct_guesses, mistakes, lives, ls_indicators)
        guess = functions.take_a_guess(word)
        for element in win_conditions:
            if guess.capitalize() == element:
                correct_guesses.append(guess.capitalize())
        guess_checked = functions.check_guess(guess, win_conditions)
        if guess_checked is True:
            correct_guesses.append(guess)
        elif guess_checked is False:
            mistakes.append(guess)
            lives = lives - 1
        functions.win_check_system(win_conditions, correct_guesses)
    functions.loose_message(word)
    time.sleep(3)


def get_life_status():
    ls_indicators = [
        life_status.lives_status_1(), life_status.lives_status_2(),
        life_status.lives_status_3(),
        life_status.lives_status_4(), life_status.lives_status_5(),
        life_status.lives_status_6()]
    return ls_indicators


def get_word():
    lines = open(
        "/home/moloch/Code/Own_Projects/Hangman/countries-and-capitals.txt").read().splitlines()
    line = random.choice(lines)
    word = line.split("|")[0].strip()
    return word


def get_lives(difficulty):
    if difficulty == "1":
        lives = 15
        return lives
    elif difficulty == "2":
        lives = 10
        return lives
    elif difficulty == "3":
        lives = 6
        return lives


def get_difficulty(force_valid_input):
    while True:
        difficulty = input(
            "Please choose a level by typing it's number!\n1: Easy\n2: Medium\n3: Hard\n4: Exit\n")
        if difficulty == "1" or difficulty == "2" or difficulty == "3":
            return difficulty
        elif difficulty == "4":
            print("Good bye!")
            exit()
        else:
            if not force_valid_input:
                return None
            print("Invalid input...")


def menu():
    os.system('clear')
    print(life_status.logo())
    difficulty = get_difficulty(True)
    word = get_word()
    lives = get_lives(difficulty)
    ls_indicators = get_life_status()
    play(word, lives, ls_indicators)


if __name__ == '__main__':
    os.system('clear')
    print("Welcome to")
    time.sleep(0.4)
    os.system("clear")
    print("Welcome to.")
    time.sleep(0.4)
    os.system('clear')
    print("Welcome to..")
    time.sleep(0.4)
    os.system("clear")
    print("Welcome to...")
    time.sleep(0.4)
    menu()
