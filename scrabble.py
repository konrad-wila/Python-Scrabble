"""Python Scrabble Game - A simple scrabble game written in Python."""
import random
import sys
# pylint: disable-msg=C0103

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


def read_tiles():
    # Task 1 function
    """Reads the tiles from the tiles.txt file and returns an array of the tiles."""
    with open("tiles.txt", "r", encoding="utf-8") as file:
        for line in file:
            tiles.append(line.strip())
    return tiles


tiles = []
tiles = read_tiles()


def read_dictionary():
    # Task 1 function
    """Reads the dictionary from the dictionary.txt file and returns a list of the words."""
    with open("dictionary.txt", "r", encoding="utf-8") as file:
        for line in file:
            dictionary.append(line.strip())
    return dictionary


dictionary = []
dictionary = read_dictionary()


def onlyEnglishLetters(word):  # noqa: Task defined function name
    # Task 2 function
    """Checks if the word only contains English letters."""
    return bool(word.isalpha())


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
    else:
        return 0


def canBeMade(word, myTiles):  # noqa: Task defined function name
    """Checks if the word can be made with the tiles."""
    for letter in word:
        if letter in myTiles:
            try:
                myTiles.remove(letter)
            except ValueError:
                return False
        else:
            return False

    return True



def isValid(word):  # noqa: Task defined function name
    """Checks if the word is a valid word."""
    try:
        if word in dictionary:
            return True
        return False
    except NameError:
        return False


def best_word():
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
    """Removes the word from the tiles."""
    try:
        for letter in word:
            tiles.remove(letter)
        return tiles
    except ValueError:
        print("You do not have the letters to make this word.")
        return tiles


def final_input_attempt(attempt_number, max_amount_of_attempts):
    """Checks if the user has reached the maximum amount of attempts."""
    if attempt_number == max_amount_of_attempts - 1:
        print("Thanks for using this application, better luck next time!!!")
        sys.exit()


def word_input():
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
    """Generates random tiles."""
    function_tiles = []
    for _ in range(7):
        function_tiles.append(random.choice(tiles))
    return function_tiles


def tile_score(function_tiles):
    """Calculates the score of the tiles."""
    score = []
    for letter in function_tiles:
        score.append(getLetterScore(letter))
    return score


def start_game():
    """Starts the game."""
    print("Generating Random Tiles ...")
    global player_tiles
    player_tiles = generate_random_tiles()
    print("Tiles: " + str(player_tiles))
    player_tile_scores = tile_score(player_tiles)
    print("Scores:" + str(player_tile_scores))
    word_input()


start_game()
