"""getWordScore function"""
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


def read_dictionary():
    # Task 1 function
    """Reads the dictionary from the dictionary.txt file and returns a list of the words."""
    with open("dictionary.txt", "r", encoding="utf-8") as file:
        for line in file:
            dictionary.append(line.strip())
    return dictionary


dictionary = []
dictionary = read_dictionary()


def getLetterScore(letter):  # noqa: Task defined function name
    # Task 4 function
    """Returns the score of the letter."""
    try:
        return int(scores[letter])
    except KeyError:
        return 0

def isValid(word):  # noqa: Task defined function name
    """Checks if the word is a valid word."""
    try:
        if word in dictionary:
            return True
        return False
    except NameError:
        return False

def getWordScore(word):  # noqa: Task defined function name
    # Task 4 function
    """Returns the score of the word."""
    if isValid(word):
        score = 0
        for letter in word:
            score += getLetterScore(letter)
        return score
    return 0
