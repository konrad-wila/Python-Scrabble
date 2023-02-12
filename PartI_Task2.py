"""Only English letters are allowed."""
# pylint: disable-msg=C0103


def onlyEnglishLetters(word):  # noqa: Task defined function name
    # Task 2 function
    # Author: Konrad Wila
    # Preconditions: word is a string
    # Postconditions: returns True if the word only contains English letters
    """Checks if the word only contains English letters."""
    return bool(word.isalpha())

def test_onlyEnglishLetters():
    """Test onlyEnglishLetters function."""
    assert onlyEnglishLetters("hello") is True
    assert onlyEnglishLetters("hello!") is False
    assert onlyEnglishLetters("hello1") is False
    assert onlyEnglishLetters("hello ") is False
    assert onlyEnglishLetters("hello-") is False
    assert onlyEnglishLetters("hello.") is False
    assert onlyEnglishLetters("hello,") is False
    assert onlyEnglishLetters("hello?") is False
    assert onlyEnglishLetters("hello/") is False
    assert onlyEnglishLetters("hello\\") is False
    assert onlyEnglishLetters("hello@") is False
    assert onlyEnglishLetters("hello#") is False
    assert onlyEnglishLetters("hello$") is False
    assert onlyEnglishLetters("hello%") is False
    assert onlyEnglishLetters("hello^") is False
    assert onlyEnglishLetters("hello&") is False
    assert onlyEnglishLetters("hello*") is False
    assert onlyEnglishLetters("hello(") is False
    assert onlyEnglishLetters("hello)") is False
    assert onlyEnglishLetters("hello_") is False
    assert onlyEnglishLetters("hello+") is False
    assert onlyEnglishLetters("hello=") is False
    assert onlyEnglishLetters("hello{") is False
    assert onlyEnglishLetters("hello}") is False
    assert onlyEnglishLetters("hello[") is False
    assert onlyEnglishLetters("hello]") is False
    assert onlyEnglishLetters("hello|") is False
    assert onlyEnglishLetters("hello:") is False
    assert onlyEnglishLetters("hello;") is False
    assert onlyEnglishLetters("hello\"") is False
    assert onlyEnglishLetters("hello'") is False
    assert onlyEnglishLetters("hello<") is False
    assert onlyEnglishLetters("hello>") is False
    assert onlyEnglishLetters("hello~") is False
    assert onlyEnglishLetters("hello`") is False
    assert onlyEnglishLetters("hello ") is False
    assert onlyEnglishLetters("hello\t") is False

test_onlyEnglishLetters()
