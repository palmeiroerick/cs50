from um import count


def test_start():
    assert count("um hello") == 1


def test_end():
    assert count("hello um") == 1


def test_signs():
    assert count("um, hello") == 1
    assert count("um. hello") == 1
    assert count("um! hello") == 1
    assert count("um? hello") == 1


def test_case():
    assert count("UM, hello") == 1
    assert count("Um, hello") == 1
    assert count("uM, hello") == 1


def test_quantity():
    assert count("hello") == 0
    assert count("um, hello, um.") == 2
    assert count("um, um, um") == 3


def test_word_with_um():
    assert count("um, number, um, three") == 2
    assert count("Um, thanks for the album.") == 1
