import os
import time


def play(word, lives):
    win_conditions = functions.get_win_conditions(word)
    mistakes = []
    correct_guesses = []
    while lives > 0:
        os.system('clear')
        prepare_round(word, correct_guesses, mistakes)
        guess = functions.take_a_guess()
        for element in win_conditions:
            if guess.capitalize() == element:
                correct_guesses.append(guess.capitalize())
        guess_checked = functions.check_guess(guess, win_conditions)
        if guess_checked is True:
            correct_guesses.append(guess)
            print("Remaining lives: " + str(lives))
        elif guess_checked is False:
            mistakes.append(guess)
            lives = lives - 1
            print("Remaining lives: " + str(lives))
        functions.win_check_system(win_conditions, correct_guesses)
    functions.loose_message()
    time.sleep(2)


def prepare_round(word, correct_guesses, mistakes):
    functions.print_board(word, correct_guesses)
    functions.print_correct_guesses(correct_guesses)
    functions.print_mistakes(mistakes)


def get_word(difficulty):
    if difficulty == "1" or difficulty == "2" or difficulty == "3":
        word = "Testing"
        return word


def get_lives(difficulty):
    if difficulty == "1":
        lives = 15
        return lives
    elif difficulty == "2":
        lives = 10
        return lives
    elif difficulty == "3":
        lives = 5
        return lives


def get_difficulty(force_valid_input):
    while True:
        difficulty = input("Please choose a level by typing it's number!\n1: Easy\n2: Medium\n3: Hard\n4: Exit\n")
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
    difficulty = get_difficulty(True)
    word = get_word(difficulty)
    lives = get_lives(difficulty)
    play(word, lives)


if __name__ == '__main__':
    print("Welcome to Hangman!")
    menu()
