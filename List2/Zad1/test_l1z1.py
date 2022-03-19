from l2z1 import is_palindrom

def test_isNotPalindrom():
    assert is_palindrom("kot") == False

def test_isPalindrom():
    assert is_palindrom("kajak") == True