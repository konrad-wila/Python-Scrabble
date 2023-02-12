"""Python Scrabble Game - A simple scrabble game written in Python."""
import random
import sys
# pylint: disable-msg=C0103

def read_scores():
    # Task 1 function
    # Author: Konrad Wila
    # Preconditions: scores.txt file exists and is in the same directory as this file and is in the correct format.
    # Postconditions: returns a dictionary of the scores
    """Reads the scores from the scores.txt file and returns a dictionary of the scores."""
    try:
        with open("scores.txt", "r", encoding="utf-8") as file:
            for line in file:
                (key, val) = line.split()
                scores[key] = val
        return scores
    except FileNotFoundError:
        print("Error: scores.txt file not found.")
        return False


scores = {}
scores = read_scores()


def read_tiles():
    # Task 1 function
    # Author: Konrad Wila
    # Preconditions: tiles.txt file exists and is in the same directory as this file and is in the correct format.
    # Postconditions: returns an array of the tiles
    """Reads the tiles from the tiles.txt file and returns an array of the tiles."""
    try:
        with open("tiles.txt", "r", encoding="utf-8") as file:
            for line in file:
                tiles.append(line.strip())
        return tiles
    except FileNotFoundError:
        print("Error: tiles.txt file not found.")
        return False


tiles = []
tiles = read_tiles()


def read_dictionary():
    # Task 1 function
    # Author: Konrad Wila
    # Preconditions: dictionary.txt file exists and is in the same directory as this file and is in the correct format.
    # Postconditions: returns a list of the words
    """Reads the dictionary from the dictionary.txt file and returns a list of the words."""
    try:
        with open("dictionary.txt", "r", encoding="utf-8") as file:
            for line in file:
                dictionary.append(line.strip())
        return dictionary
    except FileNotFoundError:
        print("Error: dictionary.txt file not found.")
        return False


dictionary = []
dictionary = read_dictionary()


def onlyEnglishLetters(word):  # noqa: Task defined function name
    # Task 2 function
    # Author: Konrad Wila
    # Preconditions: word is a string
    # Postconditions: returns True if the word only contains English letters
    """Checks if the word only contains English letters."""
    return bool(word.isalpha())


def getLetterScore(letter):  # noqa: Task defined function name
    # Task 4 function
    # Author: Konrad Wila
    # Preconditions: letter is a string
    # Postconditions: returns the score of the letter
    """Returns the score of the letter."""
    try:
        letter = letter.capitalize()
        return int(scores[letter])
    except KeyError:
        return 0


def getWordScore(word):  # noqa: Task defined function name
    # Task 4 function
    # Author: Konrad Wila
    # Preconditions: word is a string
    # Postconditions: returns the score of the word
    """Returns the score of the word."""
    word = word.upper()
    if isValid(word):
        score = 0
        for letter in word:
            score += getLetterScore(letter)
        return score
    return 0


def canBeMade(word, myTiles):  # noqa: Task defined function name
    # Task 5 function
    # Author: Konrad Wila
    # Precondition: word is a string of lowercase letters
    # Precondition: myTiles is a list of lowercase letters
    # Postcondition: returns True if word can be made with the tiles
    # Postcondition: returns False if word cannot be made with the tiles
    """Checks if the word can be made with the tiles."""
    function_player_tiles = myTiles.copy()
    for letter in word:
        if letter in function_player_tiles:
            try:
                function_player_tiles.remove(letter)
            except ValueError:
                return False
        else:
            return False

    return True



def isValid(word):  # noqa: Task defined function name
    # Task 6 function
    # Author: Konrad Wila
    # Preconditions: word is a string
    # Postconditions: returns True if the word is a valid word
    """Checks if the word is a valid word."""
    try:
        if word in dictionary:
            return True
        return False
    except NameError:
        return False


def best_word():
    # Task 7 function
    # Author: Konrad Wila
    # Preconditions: player_tiles is an array of strings
    # Postconditions: returns the highest scoring word that can be made with the tiles
    """Finds the highest scoring word that can be made with the tiles."""
    # non-assessed function (Task 7)
    # Brute force method to find the highest scoring word
    highest_scoring_word = ""
    best_score = 0
    for word in dictionary:
        if getWordScore(word) > best_score:
            if canBeMade(word, player_tiles):
                highest_scoring_word = word
                best_score = getWordScore(word)
    return highest_scoring_word


# End of Task defined functions


def remove_word_from_tiles(word):
    # Author: Konrad Wila
    # Preconditions: word is a string, tiles is an array of strings
    # Postconditions: returns an array of strings
    """Removes the word from the tiles."""
    try:
        for letter in word:
            tiles.remove(letter)
        return tiles
    except ValueError:
        print("You do not have the letters to make this word.")
        return tiles


def final_input_attempt(attempt_number, max_amount_of_attempts):
    # Author: Konrad Wila
    # Preconditions: attempt_number is an integer, max_amount_of_attempts is an integer
    # Postconditions: returns nothing, program terminates if the user has reached the maximum amount of attempts
    """Checks if the user has reached the maximum amount of attempts."""
    if attempt_number == max_amount_of_attempts - 1:
        print("Thanks for using this application, better luck next time!!!")
        sys.exit()


def word_input():
    # Author: Konrad Wila
    # Preconditions: player_tiles is an array of strings
    # Postconditions: returns a string
    """Gets word input from the user and checks if it is valid."""
    for count in range(3):
        word = input("Enter a word: ").upper()
        if word == "&&&":  # This is the secret code to exit the game
            print("Thanks for using this application, better luck next time!!!")
            sys.exit()
        elif not onlyEnglishLetters(word):
            final_input_attempt(count, 3)
            print("Only use English letters...")
        elif not isValid(word):
            final_input_attempt(count, 3)
            print("This is not a valid word.")
        elif not canBeMade(word, player_tiles):
            final_input_attempt(count, 3)
            print("You do not have the letters to make this word.")
        if onlyEnglishLetters(word) and canBeMade(word, player_tiles) and isValid(word):
            print("You got it right, this is a valid word")
            print("Score of this word is: " + str(getWordScore(word)))
            remove_word_from_tiles(word)
            break


def generate_random_tiles():
    # Author: Konrad Wila
    # Preconditions: tiles is an array of strings
    # Postconditions: returns an array of strings
    """Generates random tiles."""
    function_tiles = []
    for _ in range(7):
        function_tiles.append(random.choice(tiles))
    return function_tiles


def tile_score(function_tiles):
    # Author: Konrad Wila
    # Preconditions: function_tiles is an array of strings
    # Postconditions: returns an array of integers
    """Calculates the score of the tiles."""
    score = []
    for letter in function_tiles:
        score.append(getLetterScore(letter))
    return score


print("Generating Random Tiles ...")
player_tiles = generate_random_tiles()


def start_game():
    # Author: Konrad Wila
    # Preconditions: player_tiles is an array of strings
    # Postconditions: returns nothing
    """Starts the game."""
    print("Tiles: " + str(player_tiles))
    player_tile_scores = tile_score(player_tiles)
    print("Scores:" + str(player_tile_scores))
    word_input()


start_game()
