"""Only English letters are allowed."""
# pylint: disable-msg=C0103


def onlyEnglishLetters(word):  # noqa: Task defined function name
    # Task 2 function
    """Checks if the word only contains English letters."""
    return bool(word.isalpha())
