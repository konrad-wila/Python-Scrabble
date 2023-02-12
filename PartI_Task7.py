"""best_word functon"""
# pylint: disable-msg=C0103
import random


def read_dictionary():
    # Task 1 function
    # Precondition: The dictionary.txt file exists and is in the same directory as this file. The file contains is in the correct format.
    # Postcondition: Returns a list of the words.
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


def read_tiles():
    # Task 1 function
    # Precondition: The tiles.txt file exists and is in the same directory as this file. The file contains is in the correct format.
    # Postcondition: Returns an array of the tiles.
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


def read_scores():
    # Task 1 function
    # Precondition: The scores.txt file exists and is in the same directory as this file. The file contains is in the correct format.
    # Postcondition: Returns a dictionary of the scores.
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

def isValid(word):  # noqa: Task defined function name
    # Task 3 function
    # Preconditions: word is a string
    # Postconditions: returns True if the word is a valid word
    """Checks if the word is a valid word."""
    try:
        if word in dictionary:
            return True
        return False
    except NameError:
        return False

def getLetterScore(letter):  # noqa: Task defined function name
    # Task 4 function
    # Preconditions: letter is a string
    # Postconditions: returns the score of the letter
    """Returns the score of the letter."""
    try:
        return int(scores[letter])
    except KeyError:
        return 0


def getWordScore(word):  # noqa: Task defined function name
    # Task 4 function
    # Preconditions: word is a string
    # Postconditions: returns the score of the word
    """Returns the score of the word."""
    if isValid(word):
        score = 0
        for letter in word:
            score += getLetterScore(letter)
        return score
    return 0


def canBeMade(word, myTiles):  # noqa: Task defined function name
    # Task 5 function
    # Author: Konrad Wila
    # Preconditions: word is a string
    # Preconditions: myTiles is a list of lowercase letters
    # Postconditions: returns True if word can be made with the tiles
    # Postconditions: returns False if word cannot be made with the tiles
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


def generate_random_tiles():
    # Task 6 function
    # Author: Konrad Wila
    # Preconditions: tiles is a list of lowercase letters
    # Postconditions: returns a list of 7 random tiles
    """Generates random tiles."""
    function_tiles = []
    for _ in range(7):
        function_tiles.append(random.choice(tiles))
    return function_tiles


player_tiles = generate_random_tiles()


def best_word():
    # non-assessed function (Task 7)
    # Author: Konrad Wila
    # Brute force method to find the highest scoring word
    # Preconditions: dictionary is a list of lowercase letters
    # Preconditions: player_tiles is a list of lowercase letters
    # Postconditions: returns the highest scoring word that can be made with the tiles
    # Postconditions: returns an empty string if no word can be made with the tiles
    """Finds the highest scoring word that can be made with the tiles."""
    highest_scoring_word = ""
    best_score = 0
    for word in dictionary:
        if getWordScore(word) > best_score:
            if canBeMade(word, player_tiles):
                highest_scoring_word = word
                best_score = getWordScore(word)
    return highest_scoring_word
