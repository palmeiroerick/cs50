from twttr import shorten


def test_lower():
    assert shorten("twitter") == "twttr"
    assert shorten("aeiou") == ""


def test_upper():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("AEIOU") == ""


def test_number():
    assert shorten("CS50") == "CS50"


def test_pontuation():
    assert shorten("Hello, World!") == "Hll, Wrld!"
