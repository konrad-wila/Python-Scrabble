"""best_word functon"""
# pylint: disable-msg=C0103
import random


def read_dictionary():
    # Task 1 function
    """Reads the dictionary from the dictionary.txt file and returns a list of the words."""
    with open("dictionary.txt", "r", encoding="utf-8") as file:
        for line in file:
            dictionary.append(line.strip())
    return dictionary


dictionary = []
dictionary = read_dictionary()


def read_tiles():
    # Task 1 function
    """Reads the tiles from the tiles.txt file and returns an array of the tiles."""
    with open("tiles.txt", "r", encoding="utf-8") as file:
        for line in file:
            tiles.append(line.strip())
    return tiles


tiles = []
tiles = read_tiles()


def read_scores():
    # Task 1 function
    """Reads the scores from the scores.txt file and returns a dictionary of the scores."""
    with open("scores.txt", "r", encoding="utf-8") as file:
        for line in file:
            (key, val) = line.split()
            scores[key] = val
    return scores


scores = {}
scores = read_scores()

def isValid(word):  # noqa: Task defined function name
    """Checks if the word is a valid word."""
    try:
        if word in dictionary:
            return True
        return False
    except NameError:
        return False

def getLetterScore(letter):  # noqa: Task defined function name
    # Task 4 function
    """Returns the score of the letter."""
    try:
        return int(scores[letter])
    except KeyError:
        return 0


def getWordScore(word):  # noqa: Task defined function name
    # Task 4 function
    """Returns the score of the word."""
    if isValid(word):
        score = 0
        for letter in word:
            score += getLetterScore(letter)
        return score
    return 0


def canBeMade(word, myTiles):  # noqa: Task defined function name
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
    """Generates random tiles."""
    function_tiles = []
    for _ in range(7):
        function_tiles.append(random.choice(tiles))
    return function_tiles


player_tiles = generate_random_tiles()


def best_word():
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
