from plates import is_valid


def test_size():
    assert is_valid("A") == False
    assert is_valid("AA") == True
    assert is_valid("AAAAAA") == True
    assert is_valid("AAAAAAA") == False


def test_two_first_letter():
    assert is_valid("A0") == False
    assert is_valid("2A") == False
    assert is_valid("20") == False


def test_number_in_middle():
    assert is_valid("AA22AA") == False
    assert is_valid("AAA2AA") == False
    assert is_valid("AA2A") == False
    assert is_valid("AA2") == True
    assert is_valid("AAA222") == True


def test_zero():
    assert is_valid("AA02") == False
    assert is_valid("AA20") == True


def test_periods_spaces_and_pontuation():
    assert is_valid("AAA 22") == False
    assert is_valid("AAA.22") == False
    assert is_valid("AAA22!") == False
    assert is_valid("AAA2:2") == False
