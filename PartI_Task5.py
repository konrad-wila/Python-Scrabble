""""""
def canBeMade(word, tiles):
    """Checks if the word can be made with the tiles."""
    for letter in word:
        if letter not in tiles:
            return False
    return True