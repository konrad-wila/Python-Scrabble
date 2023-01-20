""""""
def isValid(word, dictionary):
    """Checks if the word is a valid word."""
    if word in dictionary:
        return True
    return False