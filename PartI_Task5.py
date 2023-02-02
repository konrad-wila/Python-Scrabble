"""can_be_made function"""
# pylint: disable-msg=C0103


def canBeMade(word, myTiles):  # noqa: Task defined function name
    """Checks if the word can be made with the tiles."""
    function_player_tiles = myTiles.copy()
    for letter in word:
        if letter in function_player_tiles:
            try:
                function_player_tiles.remove(letter)
            except ValueError:
                return False
        else:
            return False

    return True
