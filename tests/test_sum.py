import pytest


def test_add():
    assert 1 + 1 == 2



@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6)])
def test_sum_multiple_numbers(test_input, expected):
    assert eval(test_input) == expected



