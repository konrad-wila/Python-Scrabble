"""Python Scrabble Game - A simple scrabble game written in Python."""
import random
scores = {}
tiles = []
dictionary = []
def readScores():
    """Reads the scores from the scores.txt file and returns a dictionary of the scores."""
    with open("scores.txt", "r") as f:
        for line in f:
            (key, val) = line.split()
            scores[key] = val
    return scores
def readTiles():
    """Reads the tiles from the tiles.txt file and returns a array of the tiles."""
    with open("tiles.txt", "r") as f:
        for line in f:
            tiles.append(line.strip())
    return tiles

def readDictionary():
    """Reads the dictionary from the dictionary.txt file and returns a list of the words."""
    with open("dictionary.txt", "r") as f:
        for line in f:
            dictionary.append(line.strip())
    return dictionary

def onlyEnglishLetters(word):
    """Checks if the word only contains English letters."""
    for letter in word:
        if not letter.isalpha():
            return False
    return True

def getLetterScore(letter, scores):
    """Returns the score of the letter."""
    return scores[letter]

def getWordScore(word, scores):
    """Returns the score of the word."""
    score = 0
    for letter in word:
        score += getLetterScore(letter, scores)
    return score

def canBeMade(word, tiles):
    """Checks if the word can be made with the tiles."""
    for letter in word:
        if letter not in tiles:
            return False
    return True

def isValid(word, dictionary):
    """Checks if the word is a valid word."""
    if word in dictionary:
        return True
    return False

def removeWordFromTiles(word, tiles):
    """Removes the word from the tiles."""
    for letter in word:
        tiles.remove(letter)
    return tiles

def WordInput(tiles, dictionary, scores):
    """Gets the word from the user."""
    count = 0
    for range in range(3):
        word = input("Enter a word: ")
        if not onlyEnglishLetters(word):
            print("Only use English letters...")
        if not canBeMade(word, tiles):
            print("You do not have the letters to make this word.")
        if not isValid(word, dictionary):
            print("This is not a valid word.")
        count += 1
        if count == 3:
            print("Thanks for using this application, better luck next time!!!")
            exit
    print("You got it right, this is a valid word")
    print("Score of this word is: " + str(getWordScore(word, scores)))
    removeWordFromTiles(word, tiles)

def generateRandomTiles():
    """Generates random tiles."""
    for i in range(7):
        tiles.append(random.choice(tiles))
    return tiles

def TileScore(tiles, scores):
    """Calculates the score of the tiles."""
    score = []
    for letter in tiles:
        score.append(getLetterScore(letter, scores))
    print("Your tiles are worth " + str(score) + " points.")
    return score

def startGame():
    """Starts the game."""
    scores = readScores()
    tiles = readTiles()
    dictionary = readDictionary()
    print("Generating Random Tiles ...")
    playerTiles = generateRandomTiles()
    print("Tiles: " + str(playerTiles))
    playerTileScores = TileScore(playerTiles, scores)
    print("Scores:" + str(playerTileScores))
    WordInput(playerTiles, dictionary, scores)

startGame()
