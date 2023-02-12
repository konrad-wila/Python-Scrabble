"""Task 3"""
# pylint: disable-msg=C0103


def read_scores():
    # Task 1 function
    # Author: Konrad Wila
    # Precondition: scores.txt file exists and is in the same directory as this file and is in the correct format.
    # Postcondition: returns a dictionary of the scores
    """Reads the scores from the scores.txt file and returns a dictionary of the scores."""
    try:
        with open("scores.txt", "r", encoding="utf-8") as file:
            for line in file:
                (key, val) = line.split()
                scores[key] = val
        return scores
    except FileNotFoundError:
        print("Error: scores.txt file not found.")
        return False


scores = {}
scores = read_scores()
assert scores == {'A': '1', 'B': '3', 'C': '5', 'D': '3', 'E': '1', 'F': '5', 'G': '4', 'H': '3', 'I': '1', 'J': '10', 'K': '8', 'L': '3', 'M': '5', 'N': '3', 'O': '2', 'P': '5', 'Q': '20', 'R': '3', 'S': '3', 'T': '2', 'U': '1', 'V': '10', 'W': '12', 'X': '16', 'Y': '8', 'Z': '20'}


def getLetterScore(letter):  # noqa: Task defined function name
    # Task 4 function
    # Author: Konrad Wila
    # Preconditions: letter is a string
    # Postconditions: returns the score of the letter
    """Returns the score of the letter."""
    try:
        letter = letter.capitalize()
        return int(scores[letter])
    except KeyError:
        return 0

def test_getLetterScore():
    """Tests the getLetterScore function."""
    assert getLetterScore("a") == 1
    assert getLetterScore("b") == 3
    assert getLetterScore("c") == 5
    assert getLetterScore("d") == 3
    assert getLetterScore("e") == 1
    assert getLetterScore("f") == 5
    assert getLetterScore("g") == 4
    assert getLetterScore("h") == 3
    assert getLetterScore("i") == 1
    assert getLetterScore("j") == 10
    assert getLetterScore("k") == 8
    assert getLetterScore("l") == 3
    assert getLetterScore("m") == 5
    assert getLetterScore("n") == 3
    assert getLetterScore("o") == 2
    assert getLetterScore("p") == 5
    assert getLetterScore("q") == 20
    assert getLetterScore("r") == 3
    assert getLetterScore("s") == 3
    assert getLetterScore("t") == 2
    assert getLetterScore("u") == 1
    assert getLetterScore("v") == 10
    assert getLetterScore("w") == 12
    assert getLetterScore("x") == 16
    assert getLetterScore("y") == 8
    assert getLetterScore("z") == 20
    assert getLetterScore("A") == 1
    assert getLetterScore("B") == 3
    assert getLetterScore("C") == 5
    assert getLetterScore("D") == 3
    assert getLetterScore("E") == 1
    assert getLetterScore("F") == 5
    assert getLetterScore("G") == 4
    assert getLetterScore("H") == 3
    assert getLetterScore("I") == 1
    assert getLetterScore("J") == 10
    assert getLetterScore("K") == 8
    assert getLetterScore("L") == 3
    assert getLetterScore("M") == 5
    assert getLetterScore("N") == 3
    assert getLetterScore("O") == 2
    assert getLetterScore("P") == 5
    assert getLetterScore("Q") == 20
    assert getLetterScore("R") == 3
    assert getLetterScore("S") == 3
    assert getLetterScore("T") == 2
    assert getLetterScore("U") == 1
    assert getLetterScore("V") == 10
    assert getLetterScore("W") == 12
    assert getLetterScore("X") == 16
    assert getLetterScore("Y") == 8
    assert getLetterScore("Z") == 20
    assert getLetterScore("1") == 0
    assert getLetterScore("2") == 0
    assert getLetterScore("3") == 0
    assert getLetterScore("4") == 0
    assert getLetterScore("5") == 0
    assert getLetterScore("6") == 0
    assert getLetterScore("7") == 0
    assert getLetterScore("8") == 0
    assert getLetterScore("9") == 0
    assert getLetterScore("0") == 0
    assert getLetterScore(" ") == 0
    assert getLetterScore("") == 0
    assert getLetterScore("a1") == 0
    assert getLetterScore("a ") == 0
    assert getLetterScore(" a") == 0
    assert getLetterScore("a a") == 0
    assert getLetterScore("a1a") == 0
    assert getLetterScore("a1 ") == 0
    assert getLetterScore(" a1") == 0
    assert getLetterScore("a 1") == 0
    assert getLetterScore("a 1a") == 0
    assert getLetterScore("a 1 a") == 0
    assert getLetterScore("a 1 a ") == 0
    assert getLetterScore(" a 1 a") == 0
    assert getLetterScore(" a 1 a ") == 0

test_getLetterScore()
