import pytest

from task1 import get_continued_fraction


@pytest.mark.parametrize(
    "test_fraction,result",
    [
        ("239/30", "7 1 29"),
        ("-9/4", "-3 1 3"),
        ("0/10", "0"),
        ("5/10", "0 2"),
        ("5/1", "5"),
        ("5/5", "1"),
    ],
)
def test_positive(test_fraction, result):
    assert get_continued_fraction(test_fraction) == result


def test_zero_division():
    with pytest.raises(ZeroDivisionError) as err:
        _ = get_continued_fraction("1/0")
    assert "integer division or modulo by zero" in str(err.value)


@pytest.mark.parametrize("test_fraction", ["9/-4", "123.4", "", "abc", "a/b"])
def test_wrong_format(test_fraction):
    with pytest.raises(ValueError):
        get_continued_fraction(test_fraction)
