from seasons import get_date
from datetime import date


def test_get_date():
    assert get_date("1990-01-01") == date(1990, 1, 1)
    assert get_date("2010-10-10") == date(2010, 10, 10)
    assert get_date("2025-02-15") == date(2025, 2, 15)
