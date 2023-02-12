"""can_be_made function"""
# pylint: disable-msg=C0103


def canBeMade(word, myTiles):  # noqa: Task defined function name
    # Author: Konrad Wila
    # Precondition: word is a string of lowercase letters
    # Precondition: myTiles is a list of lowercase letters
    # Postcondition: returns True if word can be made with the tiles
    # Postcondition: returns False if word cannot be made with the tiles
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

def test_canBeMade():
    """Test canBeMade function."""
    assert canBeMade("cat", ["c", "a", "s"]) is False
    assert canBeMade("cat", ["c", "a", "t"]) is True
    assert canBeMade("cat", ["c", "a", "t", "t"]) is True
    assert canBeMade("cat", ["c", "a", "t", "t", "t"]) is True
    assert canBeMade("cat", ["c", "a", "t", "t", "t", "t"]) is True
    assert canBeMade("cat", ["c", "a", "t", "t", "t", "t", "t"]) is True
    assert canBeMade("cat", ["c", "a", "t", "t", "t", "t", "t", "t"]) is True
    assert canBeMade("cat", ["c", "a", "t", "t", "t", "t", "t", "t", "t"]) is True
    assert canBeMade("cat", ["c", "a", "t", "t", "t", "t", "t", "t", "t", "t"]) is True
    assert canBeMade("cat", ["c", "a", "t", "t", "t", "t", "t", "t", "t", "t", "t"]) is True
    assert canBeMade("cat", ["c", "a", "t", "t", "t", "t", "t", "t", "t", "t", "t", "t"]) is True

test_canBeMade()
