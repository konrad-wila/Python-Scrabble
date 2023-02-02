"""getWordScore function"""
# pylint: disable-msg=C0103


def read_scores():
    # Task 1 function
    # Author: Konrad Wila
    # Precondition: scores.txt file exists and is in the same directory as this file and is in the correct format.
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
    # Author: Konrad Wila
    # Precondition: dictionary.txt file exists and is in the same directory as this file and is in the correct format.
    # Postcondition: returns a list of the words
    """Reads the dictionary from the dictionary.txt file and returns a list of the words."""
    with open("dictionary.txt", "r", encoding="utf-8") as file:
        for line in file:
            dictionary.append(line.strip())
    return dictionary


dictionary = []
dictionary = read_dictionary()


def getLetterScore(letter):  # noqa: Task defined function name
    # Task 4 function
    # Author: Konrad Wila
    # Preconditions: letter is a string
    # Postconditions: returns the score of the letter
    """Returns the score of the letter."""
    try:
        return int(scores[letter])
    except KeyError:
        return 0

def isValid(word):  # noqa: Task defined function name
    # Task 6 function
    # Author: Konrad Wila
    # Preconditions: word is a string
    # Postconditions: returns True if the word is a valid word
    """Checks if the word is a valid word."""
    try:
        if word in dictionary:
            return True
        return False
    except NameError:
        return False

def getWordScore(word):  # noqa: Task defined function name
    # Task 4 function
    # Author: Konrad Wila
    # Preconditions: word is a string
    # Postconditions: returns the score of the word
    """Returns the score of the word."""
    if isValid(word):
        score = 0
        for letter in word:
            score += getLetterScore(letter)
        return score
    return 0
