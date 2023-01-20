"""getWordScore function"""
def getWordScore(word, scores):
    """Returns the score of the word."""
    score = 0
    for letter in word:
        score += getLetterScore(letter, scores)
    return score