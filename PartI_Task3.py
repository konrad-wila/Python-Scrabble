"""Task 3"""
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

def getLetterScore(letter):  # noqa: Task defined function name
    # Task 4 function
    """Returns the score of the letter."""
    try:
        return int(scores[letter])
    except KeyError:
        return 0
