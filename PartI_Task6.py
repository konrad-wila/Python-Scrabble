"""is_valid function"""
# pylint: disable-msg=C0103


def read_dictionary():
    # Task 1 function
    """Reads the dictionary from the dictionary.txt file and returns a list of the words."""
    with open("dictionary.txt", "r", encoding="utf-8") as file:
        for line in file:
            dictionary.append(line.strip())
    return dictionary


dictionary = []
dictionary = read_dictionary()

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

def isValid(word, MyTiles, dictionary):  # noqa: Task defined function name
    """Checks if the word is a valid word."""
    try:
        if word in dictionary:
            return True
        return canBeMade(word, MyTiles)
    except NameError:
        return False
