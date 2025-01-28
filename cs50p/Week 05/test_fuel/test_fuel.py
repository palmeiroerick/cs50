import pytest

from fuel import convert, gauge


def test_ValueError_in_convert():
    with pytest.raises(ValueError):
        convert("cat")

    with pytest.raises(ValueError):
        convert("4/3")


def test_ZeroDivisionError_in_convert():
    with pytest.raises(ZeroDivisionError):
        convert("0/0")


def test_convert():
    assert convert("4/4") == 100
    assert convert("0/4") == 0
    assert convert("2/4") == 50
    assert convert("5/9") == 56
    assert convert("1/100") == 1
    assert convert("99/100") == 99


def test_gauge():
    assert gauge(100) == "F"
    assert gauge(0) == "E"
    assert gauge(50) == "50%"
    assert gauge(56) == "56%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
