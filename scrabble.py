"""Python Scrabble Game - A simple scrabble game written in Python."""
import random
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
    """Reads the tiles from the tiles.txt file and returns a array of the tiles."""
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
    for letter in word:
        if not letter.isalpha():
            return False
    return True

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

def is_valid(word, dictionary):
    """Checks if the word is a valid word."""
    if word in dictionary:
        return True
    return False

def remove_word_from_tiles(word):
    """Removes the word from the tiles."""
    for letter in word:
        tiles.remove(letter)
    return tiles

def word_input():
    """Gets the word from the user."""
    for count in range(3):
        word = input("Enter a word: ")
        if not only_english_letters(word):
            print("Only use English letters...")
        if not can_be_made(word):
            print("You do not have the letters to make this word.")
        if not is_valid(word, dictionary):
            print("This is not a valid word.")
        if count == 3:
            print("Thanks for using this application, better luck next time!!!")
            exit
    print("You got it right, this is a valid word")
    print("Score of this word is: " + str(get_word_score(word, scores)))
    remove_word_from_tiles(word)

def generate_random_tiles():
    """Generates random tiles."""
    for _ in range(7):
        tiles.append(random.choice(tiles))
    return tiles

def tile_score(tiles, scores):
    """Calculates the score of the tiles."""
    score = []
    for letter in tiles:
        score.append(get_letter_score(letter))
    print("Your tiles are worth " + str(score) + " points.")
    return score
def start_game():
    """Starts the game."""
    scores = read_scores()
    tiles = read_tiles()
    dictionary = read_dictionary()
    print("Generating Random Tiles ...")
    playerTiles = generate_random_tiles()
    print("Tiles: " + str(playerTiles))
    playerTileScores = tile_score(playerTiles, scores)
    print("Scores:" + str(playerTileScores))
    word_input()

start_game()
