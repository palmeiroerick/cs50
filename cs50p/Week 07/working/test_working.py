import pytest

from working import convert


def test_format():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")


def test_PM_to_AM():
    assert convert("5:00 PM to 9:00 AM") == "17:00 to 09:00"


def test_invalid_time():
    with pytest.raises(ValueError):
        convert("5:60 PM to 9:00 AM")
    with pytest.raises(ValueError):
        convert("5:00 PM to 13:00 AM")


def test_12_AM():
    assert convert("12 AM to 5:00 PM") == "00:00 to 17:00"


def test_12_PM():
    assert convert("9:00 AM to 12 PM") == "09:00 to 12:00"
