"""is_valid function"""
# pylint: disable-msg=C0103


def read_dictionary():
    # Task 1 function
    # Author: Konrad Wila
    # Precondition: dictionary.txt file exists in the same directory as this file and is in the correct format.
    # Postcondition: returns a list of the words
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

def canBeMade(word, myTiles):  # noqa: Task defined function name
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

def isValid(word, MyTiles, dictionary):  # noqa: Task defined function name
    # Author: Konrad Wila
    # Precondition: word is a string of lowercase letters
    # Precondition: myTiles is a list of lowercase letters
    # Postcondition: returns True if word is a valid word
    # Postcondition: returns False if word is not a valid word
    # Postcondition: returns False if word cannot be made with the tiles
    """Checks if the word is a valid word."""
    try:
        if word in dictionary:
            return True
        return canBeMade(word, MyTiles)
    except NameError:
        return False

def test_isValid():
    assert isValid("hello", ["h", "e", "l", "l", "o"], dictionary) == True
    assert isValid("hello", ["h", "e", "l", "l", "o", "o"], dictionary) == True
    assert isValid("hello", ["h", "e", "l", "l", "o"], dictionary) == True
    assert isValid("hello", ["h", "e", "l", "l", "l"], dictionary) == False

test_isValid()
