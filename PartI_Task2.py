"""Only English letters are allowed."""

def onlyEnglishLetters(word):
    """Checks if the word only contains English letters."""
    for letter in word:
        if not letter.isalpha():
            return False
    return True