"""Read in Scores, Tile and Dictionary"""
def readScores():
    """Reads the scores from the scores.txt file and returns a dictionary of the scores."""
    with open("scores.txt", "r") as f:
        for line in f:
            (key, val) = line.split()
            scores[key] = val
    return scores
def readTiles():
    """Reads the tiles from the tiles.txt file and returns a array of the tiles."""
    with open("tiles.txt", "r") as f:
        for line in f:
            tiles.append(line.strip())
    return tiles

def readDictionary():
    """Reads the dictionary from the dictionary.txt file and returns a list of the words."""
    with open("dictionary.txt", "r") as f:
        for line in f:
            dictionary.append(line.strip())
    return dictionary