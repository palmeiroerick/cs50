from numb3rs import validate


def test_string():
    assert validate("cat") == False


def test_quantity():
    assert validate("127.0.1") == False
    assert validate("127.0.0.0.1") == False


def test_range():
    assert validate("0.0.0.0") == True
    assert validate("127.0.0.1") == True
    assert validate("256.0.0.1") == False
    assert validate("127.256.0.1") == False
    assert validate("127.0.256.1") == False
    assert validate("127.0.0.256") == False
