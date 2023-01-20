"""Python Scrabble Game - A simple scrabble game written in Python."""
import random
import sys


def read_scores():
    """Reads the scores from the scores.txt file and returns a dictionary of the scores."""
    with open("scores.txt", "r", encoding="utf-8") as file:
        for line in file:
            (key, val) = line.split()
            scores[key] = val
    return scores


scores = {}
scores = read_scores()


def read_tiles():
    """Reads the tiles from the tiles.txt file and returns an array of the tiles."""
    with open("tiles.txt", "r", encoding="utf-8") as file:
        for line in file:
            tiles.append(line.strip())
    return tiles


tiles = []
tiles = read_tiles()


def read_dictionary():
    """Reads the dictionary from the dictionary.txt file and returns a list of the words."""
    with open("dictionary.txt", "r", encoding="utf-8") as file:
        for line in file:
            dictionary.append(line.strip())
    return dictionary


dictionary = []
dictionary = read_dictionary()


def only_english_letters(word):
    """Checks if the word only contains English letters."""
    return bool(word.isalpha())


def get_letter_score(letter):
    """Returns the score of the letter."""
    return scores[letter]


def get_word_score(word):
    """Returns the score of the word."""
    score = 0
    for letter in word:
        score += get_letter_score(letter)
    return score


def can_be_made(word):
    """Checks if the word can be made with the tiles."""
    for letter in word:
        if letter not in tiles:
            return False
    return True


def is_valid(word):
    """Checks if the word is a valid word."""
    if word in dictionary:
        return True
    return False


def remove_word_from_tiles(word):
    """Removes the word from the tiles."""
    for letter in word:
        tiles.remove(letter)
    return tiles


def final_input_attempt(attempt_number, max_amount_of_attempts):
    """Checks if the user has reached the maximum amount of attempts."""
    if attempt_number == max_amount_of_attempts:
        print("Thanks for using this application, better luck next time!!!")
        sys.exit()


def word_input():
    """Gets word input from the user and checks if it is valid."""
    for count in range(3):
        word = input("Enter a word: ").upper()
        if not only_english_letters(word):
            final_input_attempt(count, 3)
            print("Only use English letters...")
        elif not is_valid(word):
            final_input_attempt(count, 3)
            print("This is not a valid word.")
        elif not can_be_made(word):
            final_input_attempt(count, 3)
            print("You do not have the letters to make this word.")
        if only_english_letters(word) and can_be_made(word) and is_valid(word):
            print("You got it right, this is a valid word")
            print("Score of this word is: " + str(get_word_score(word)))
            remove_word_from_tiles(word)
            break


def generate_random_tiles():
    """Generates random tiles."""
    function_tiles = []
    for _ in range(7):
        function_tiles.append(random.choice(tiles))
    return function_tiles


def tile_score(function_tiles):
    """Calculates the score of the tiles."""
    score = []
    for letter in function_tiles:
        score.append(get_letter_score(letter))
    return score


def start_game():
    """Starts the game."""
    print("Generating Random Tiles ...")
    player_tiles = generate_random_tiles()
    print("Tiles: " + str(player_tiles))
    player_tile_scores = tile_score(player_tiles)
    print("Scores:" + str(player_tile_scores))
    word_input()


start_game()
