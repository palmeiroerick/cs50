from bank import value


def test_hello():
    assert value("Hello") == 0
    assert value("Hello, Kramer!") == 0


def test_greeting_beginning_with_h():
    assert value("Hey") == 20
    assert value("How you doing?") == 20


def test_something_else():
    assert value("What's happening?") == 100
    assert value("What’s up?") == 100
