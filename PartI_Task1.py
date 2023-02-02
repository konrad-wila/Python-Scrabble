"""Read in Scores, Tile and Dictionary"""
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


def read_tiles():
    # Task 1 function
    """Reads the tiles from the tiles.txt file and returns an array of the tiles."""
    with open("tiles.txt", "r", encoding="utf-8") as file:
        for line in file:
            tiles.append(line.strip())
    return tiles


tiles = []
tiles = read_tiles()


def read_dictionary():
    # Task 1 function
    """Reads the dictionary from the dictionary.txt file and returns a list of the words."""
    with open("dictionary.txt", "r", encoding="utf-8") as file:
        for line in file:
            dictionary.append(line.strip())
    return dictionary


dictionary = []
dictionary = read_dictionary()
